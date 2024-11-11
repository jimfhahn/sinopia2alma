# sinopia2alma

# Alma RDF/XML 
To generate RDF/XML for Alma Work or Instance start the binder and navigate to the notebooks. If posting to Alma, the system requires the Work resource to be sent in first before the Instance. Run the notebook for Work before Instance when posting to Alma.

# MARCXML 
To preview MARCXML from sinopia RDF using the [Library of Congress transformation code](https://github.com/lcnetdev/bibframe2marc) simply run the rdf2marcxml.ipynb notebook. 

Note: In the notebook replace the URI with your sinopia Instance URI. The setup uses the Work linked to that Instance URI.

# Alma RDF to OCLC (experimental)
This is a pilot test to generate [OCLC RDF structure](https://help.oclc.org/Metadata_Services/WorldShare_Collection_Manager/Data_sync_collections/Prepare_your_data/Structure_BIBFRAME_data) from sinopia RDF. Available by way on an SRU query, examples in the rdf2oclc.ipynb notebook.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jimfhahn/sinopia2alma/main)

# Notebooks
## rdf2marcxml.ipynb
## work_alma_s3.ipynb
## instance_alma_s3.ipynb
## rdf2oclc.ipynb 


