# sinopia2alma

## Alma RDF/XML 
To generate RDF/XML for Alma Work or Instance start the binder and navigate to the notebooks. If posting to Alma, the system requires the Work resource to be sent in first before the Instance. Run the notebook for Work first, then the Instance notebook.

## MARCXML 
To preview MARCXML from sinopia RDF using the [Library of Congress transformation code](https://github.com/lcnetdev/bibframe2marc) simply run the rdf2marcxml.ipynb notebook. 

Note: In the notebook replace the URI with your sinopia Instance URI. The setup uses the Work linked to that Instance URI.

## Alma BF to OCLC (experimental)
This is a pilot test to generate [OCLC RDF structure](https://help.oclc.org/Metadata_Services/WorldShare_Collection_Manager/Data_sync_collections/Prepare_your_data/Structure_BIBFRAME_data) from Alma BF. Available by way of an SRU query, examples in the almabf2oclc.ipynb notebook.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jimfhahn/sinopia2alma/main)

## Notebooks

* [rdf2marcxml.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/rdf2marcxml.ipynb)
* [work_alma.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/work2alma.ipynb)
* [instance_alma.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/work2alma.ipynb)
* [almabf2oclc.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/almabf2oclc.ipynb)


