# sinopia2alma [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jimfhahn/sinopia2alma/main)
A collection of Jupyter notebooks to convert Sinopia RDF to Alma RDF/XML and MARCXML. Also includes a pilot test to generate OCLC RDF from Alma BF.

### Before running, add a .env file to the root directory with the following:
```
ALMA_API_KEY="apikey"
ALMA_API_HOST="url"
```
Region details and API key generation for your Alma system can be found here: [Alma Developer Network](https://developers.exlibrisgroup.com/alma/apis). Consider using Alma Sandbox API for testing. The API key should have read/write permissions for bib operations.
### Region info:

| Region        | URL                                      |
|---------------|------------------------------------------|
| North America | https://api-na.hosted.exlibrisgroup.com  |
| Europe        | https://api-eu.hosted.exlibrisgroup.com  |
| Asia Pacific  | https://api-ap.hosted.exlibrisgroup.com  |
| Canada        | https://api-ca.hosted.exlibrisgroup.com  |
| China         | https://api-cn.hosted.exlibrisgroup.com.cn |

## Alma RDF/XML 
To generate RDF/XML for Alma Work or Instance start the binder and navigate to the notebooks. If posting to Alma, the system requires the Work resource to be sent in first before the Instance. Run the notebook for Work first, then the Instance notebook.

## MARCXML 
To preview MARCXML from sinopia RDF using the [Library of Congress transformation code](https://github.com/lcnetdev/bibframe2marc) simply run the rdf2marcxml.ipynb notebook. 

Note: In the notebook replace the URI with your sinopia Instance URI. The setup uses the Work linked to that Instance URI.

## Alma BF to OCLC (experimental)
This is a pilot test to generate [OCLC RDF structure](https://help.oclc.org/Metadata_Services/WorldShare_Collection_Manager/Data_sync_collections/Prepare_your_data/Structure_BIBFRAME_data) from Alma BF. Available by way of an SRU query, examples in the almabf2oclc.ipynb notebook.


## Notebooks
* [work_alma.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/work2alma.ipynb)

* [instance_alma.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/work2alma.ipynb)

* [rdf2marcxml.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/rdf2marcxml.ipynb)

* [almabf2oclc.ipynb](https://github.com/jimfhahn/sinopia2alma/blob/main/almabf2oclc.ipynb)


