from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF
from name_space.alma_ns import alma_namespaces
from lxml import etree as ET
from copy import deepcopy


def lc_bfxml_work(uri):
    instance_uri = URIRef(uri)
    work_uri = None
    instance_graph = Graph()
    work_graph = Graph()
    instance_graph.parse(instance_uri)
    # Define the bf namespace
    bf = Namespace("http://id.loc.gov/ontologies/bibframe/")

    for prefix, url in alma_namespaces:
        work_graph.bind(prefix, url)
    work_uri = instance_graph.value(
        subject=URIRef(instance_uri), predicate=bf.instanceOf
        )
    work_uri = URIRef(work_uri)
    # Explicitly state that work_uri is of type bf:Work
    work_graph.add((work_uri, RDF.type, bf.Work))

    # parse the work graph
    work_graph.parse(work_uri)

    # add the instance to the work graph
    # this isn't required in Alma, but OCLC requires this as part of the concise bounded description.
    work_graph.add((work_uri, bf.hasInstance, URIRef(instance_uri)))

    # serialize the work graph
    bfwork_alma_xml = work_graph.serialize(format="pretty-xml", encoding="utf-8")
    tree = ET.fromstring(bfwork_alma_xml)
    # save the work graph to a file
    with open("work_graph.xml", "wb") as f:
        f.write(bfwork_alma_xml)

    # Parse the XML file
    tree = ET.parse('work_graph.xml')
    work_graph = tree.getroot()

    # Define namespaces
    namespaces = {
        'bf': 'http://id.loc.gov/ontologies/bibframe/',
        'bflc': 'http://id.loc.gov/ontologies/bflc/',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',   
    }

    # Find all bf:Work elements
    works = work_graph.xpath('//bf:Work', namespaces=namespaces)

    # Create a list to keep track of works to remove
    works_to_remove = []

    for work in works:
        work_about = work.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')

        if work_about:
            # Find the bf:relatedTo elements that are directly linked to a bf:Work element
            related_to_elements = work_graph.xpath(f'//bf:relatedTo[@rdf:resource="{work_about}"]', namespaces=namespaces)

            cloned = False  # Flag to track if the work has been cloned

            for related_to in related_to_elements:
                # Check if the bf:relatedTo element is within a bflc:Relationship
                relationship = related_to.getparent()
                if relationship.tag in ('{http://id.loc.gov/ontologies/bflc/}Relationship', '{http://id.loc.gov/ontologies/bibframe/}Relationship'):
                    # Check if the bflc:Relationship or bf:Relationship contains a bf:Work element
                    if relationship.find('bf:relatedTo/bf:Work', namespaces=namespaces) is not None:

                        # Remove the rdf:resource attribute from the bf:relatedTo element
                        related_to.attrib.pop('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource', None)

                        # Check if the bf:Work element already exists within bf:relatedTo
                        existing_work = related_to.find('bf:Work', namespaces=namespaces)
                        if existing_work is None:
                            # Clone the bf:Work element and append it under the bf:relatedTo element
                            cloned_work = deepcopy(work)
                            related_to.append(cloned_work)
                            cloned = True  # Set the flag to True

            # Add the original bf:Work element to the list of works to remove only if it was cloned
            if cloned:
                works_to_remove.append(work)

    # Remove the original bf:Work elements
    for work in works_to_remove:
        work.getparent().remove(work)

    # Serialize the modified XML
    ET.ElementTree(work_graph).write('bfwork_alma.xml', pretty_print=True, encoding='utf-8')


    # open the file and parse the XML
    tree = ET.parse("bfwork_alma.xml")
    xslt = ET.parse("marc_xml/xsl/normalize-work-sinopia2alma.xsl")
    transform = ET.XSLT(xslt)
    alma_xml = transform(tree)
    alma_xml = ET.tostring(
            alma_xml, pretty_print=True, encoding="utf-8"
            )
    # save the xml to a file
    with open("alma-work.xml", "wb") as f:
        f.write(alma_xml)


def remove_last_line():
    with open("bfwork_alma.xml", 'r') as file:
        lines = file.readlines()

    # remove last non-empty line if it is a closing RDF tag
    if lines[-1].strip() == "</rdf:RDF>":
        lines.pop()

    with open("bfxml_work.xml", 'w') as file:
        file.writelines(lines)
