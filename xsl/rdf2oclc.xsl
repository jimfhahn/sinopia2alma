<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:bf="http://id.loc.gov/ontologies/bibframe/"
    xmlns:bflc="http://id.loc.gov/ontologies/bflc/"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:skos="http://www.w3.org/2004/02/skos/core#"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:cc="http://creativecommons.org/ns#"
    xmlns:foaf="http://xmlns.com/foaf/0.1"
    xmlns:sinopia="http://sinopia.io/vocabulary/"
    exclude-result-prefixes="xsl">

    <xsl:output method="xml" indent="yes"/>

    <!-- Root template -->
    <xsl:template match="/">
        <rdf:RDF>
            <xsl:apply-templates select="rdf:RDF/bf:Instance"/>
            <xsl:apply-templates select="rdf:RDF/bf:Work"/>
        </rdf:RDF>
    </xsl:template>

    <!-- Template for bf:Instance -->
    <xsl:template match="bf:Instance">
        <bf:Instance rdf:about="{@rdf:about}">
            <xsl:apply-templates select="node()|@*"/>
        </bf:Instance>
    </xsl:template>

    <!-- Template for bf:Work -->
    <xsl:template match="bf:Work">
        <bf:Work rdf:about="{@rdf:about}">
            <xsl:apply-templates select="node()|@*"/>
        </bf:Work>
    </xsl:template>

    <!-- Template for transforming bf:instanceOf with nested rdf:Description -->
    <xsl:template match="bf:instanceOf[rdf:Description]">
        <bf:instanceOf rdf:resource="{rdf:Description/@rdf:about}"/>
    </xsl:template>

    <!-- Template to remove rdf:nodeID attributes -->
    <xsl:template match="@rdf:nodeID"/>

    <!-- Copy all other elements and attributes -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>