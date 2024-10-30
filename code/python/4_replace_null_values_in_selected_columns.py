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
import numpy as np

def replace_null_values_in_selected_columns(source_gpkg, target_gpkg):
    
    try:
        # get all layers in 
        gadm_layers = gpd.list_layers(source_gpkg)['name'].tolist()
        
        for g in gadm_layers:

            gdf = gpd.read_file(source_gpkg,layer=g)

            for gmfn in GADM_MODEL_FIELD_NAMES:
                if gmfn in list(gdf):
                    message = f"Layer {g} has a column that needs to be fixed: {gmfn}"
                    logging.info(message)
                    gdf[g] = gdf[g].replace("NA", np.nan)

                    result = gdf.to_file("output.json", driver="GeoJSON", layer=g)
                else:
                    pass
    except Exception as e:
        message = f"Exception trying to replace nulls in layer {g}: {e}"
        logging.error(message)
    
if __name__ == "__main__":

    # CONSTANTS AND MAGICS

    GADM_GPKG = VECTOR_SPATIAL_DATA_SUBDIRECTORY / 'gadm_410-levels' / 'gadm_410-levels.gpkg'
    GADM_GPKG_CORRECTED = VECTOR_SPATIAL_DATA_SUBDIRECTORY / 'gadm_410-levels' / 'gadm_410-levels-nulls_fixed.gpkg'

    logging.info("Step 4: Replace Null Values in GADM Foreign Key Columns")
    replace_null_values_in_selected_columns(source_gpkg=GADM_GPKG, target_gpkg=GADM_GPKG_CORRECTED)






