from rdflib import Graph, Namespace, URIRef
from name_space.alma_ns import alma_namespaces
import sys
import lxml.etree as ET


def lc_bfxml_instance(instance_uri):
    instance_uri = URIRef(instance_uri)
    work_uri = None
    instance_graph = Graph()
    instance_graph.parse(instance_uri)
    # Define the bf and bflc namespaces
    bf = Namespace("http://id.loc.gov/ontologies/bibframe/")
    # Bind the namespaces to the instance graph
    for prefix, url in alma_namespaces:
        instance_graph.bind(prefix, url)
    # Get the work URI from the instance graph
    work_uri = instance_graph.value(subject=instance_uri, predicate=bf.instanceOf)
    # check if the work_uri is none
    if work_uri is None:
        print("No work URI found for this instance.")
        sys.exit()

    # Ensure work_uri is a URIRef
    work_uri = URIRef(work_uri)

    # Remove any triples where work_uri is the subject
    instance_graph.remove((work_uri, None, None))
    # Serialize the instance graph
    instance_alma_xml = instance_graph.serialize(format="pretty-xml", encoding="utf-8")

    tree = ET.fromstring(instance_alma_xml)
    # apply xslt to normalize instance
    xslt = ET.parse("marc_xml/xsl/normalize-instance-sinopia2alma.xsl")
    transform = ET.XSLT(xslt)
    instance_alma_xml = transform(tree)
    instance_alma_xml = ET.tostring(
            instance_alma_xml, pretty_print=True, encoding="utf-8"
            )
    # save the xml to a file
    with open("lc_bfxml_instance.xml", "wb") as f:
        f.write(instance_alma_xml)


def remove_rdf_header():
    filename = "lc_bfxml_instance.xml"
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Find the line with the opening '<rdf:RDF'
    start = next(i for i, line in enumerate(lines) if '<rdf:RDF' in line)

    # Find the line with the closing '>'
    end = next(i for i, line in enumerate(lines[start:], start=start) if '>' in line)

    # Remove all lines from start to end
    lines = lines[end+1:]

    with open(filename, 'w') as file:
        file.writelines(lines)
