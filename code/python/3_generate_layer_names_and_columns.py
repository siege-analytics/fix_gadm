__author__ = "Dheeraj Chand"
__copyright__ = "Siege Analytics, 2024"
__credits__ = ["Dheeraj Chand"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dheeraj Chand"
__email__ = "dheeraj@siegeanalytics.com"
__status__ = "Production"


# imports

from utilities import *
from settings import *
import logging
import pathlib
import geopandas as gpd
import json

def generate_layers_and_attributes(target_gpkg, target_json):
    
    # get all layers in 
    gadm_layers = gpd.list_layers(target_gpkg)['name'].tolist()
    layer_name_and_attributes = {}
    
    # create the dictionary of columns and values
    for g in gadm_layers:

        gdf = gpd.read_file(target_gpkg,layer=g)
        layer_name_and_attributes[g] = list(gdf)
    
    with open(LAYERS_AND_ATTRIBUTES, 'w') as json_file:
        json.dump(layer_name_and_attributes, json_file, indent=4)
    
if __name__ == "__main__":

    # CONSTANTS AND MAGICS

    GADM_GPKG = VECTOR_SPATIAL_DATA_SUBDIRECTORY / 'gadm_410-levels' / 'gadm_410-levels.gpkg'
    LAYERS_AND_ATTRIBUTES = OUTPUT_DIRECTORY / 'layers_and_attributes.json'

    logging.info("Step 3: Generate JSON of GADM Layers and Columns")
    generate_layers_and_attributes(target_gpkg=GADM_GPKG, target_json=LAYERS_AND_ATTRIBUTES)





