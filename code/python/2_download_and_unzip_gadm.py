__credits__ = ['Dheeraj Chand']
__version__ = '0.1.2'
__maintainer__ = 'Dheeraj Chand'
__email__ = 'dheeraj@siegeanalytics.com'
__status__ = 'Dev'


from utilities import *
from settings import *
import logging
import pathlib

def download_gadm_to_path(target_url, target_path):
    try:
        message = f"Going to download {target_url}"
        logging.info(message)
        
        download_file(url=GADM_URL, local_filename=target_path)
        logging.info(message)
        return target_path
    except Exception as e:
        message = f"Ran into an Exception trying to download {GADM_URL}: {e}"
        logging.error(e)
        return False


def unzip_gadm(target_zipfile):
    try:
        target_zipfile = pathlib.Path(target_zipfile)
        unzip_file_to_its_own_directory(target_zipfile)
    except Exception as e:
        message = f"Ran into an Exception trying to unzip {target_zipfile}: {e}"
        logging.error(e)
        return False

if __name__ == "__main__":
    logging.info("Step 2: Fetch GADM file and unzip it")
    target_url = GADM_URL
    file_name = GADM_URL.split("/")[-1] 
    target_path = str(VECTOR_SPATIAL_DATA_SUBDIRECTORY / file_name)
    
    # download_gadm_to_path(target_url=target_url, target_path=target_path)
    unzip_gadm(target_zipfile=target_path)