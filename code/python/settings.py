__author__ = "Dheeraj Chand"
__copyright__ = "Siege Analytics, 2024"
__credits__ = ["Dheeraj Chand"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dheeraj Chand"
__email__ = "dheeraj@siegeanalytics.com"
__status__ = "Production"

import pathlib

# going to build paths for use relative to the settings file

ALL_PARENTS = list(pathlib.Path(__file__).parents)

PYTHON_DIRECTORY = ALL_PARENTS[0]             # directory that contains the settings file
CODE_DIRECTORY = ALL_PARENTS[1]           # directory that contains the settings directory and manage.py
PROJECT_DIRECTORY = ALL_PARENTS[2]
# now build paths to useful directories

# Data

DATA_DIRECTORY = PROJECT_DIRECTORY / 'data'
SPATIAL_DATA_SUBDIRECTORY = DATA_DIRECTORY / 'spatial'
TABULAR_DATA_SUBDIRECTORY = DATA_DIRECTORY / 'tabular'
VECTOR_SPATIAL_DATA_SUBDIRECTORY = SPATIAL_DATA_SUBDIRECTORY / 'vector'
RASTER_SPATIAL_DATA_SUBDIRECTORY = SPATIAL_DATA_SUBDIRECTORY / 'raster'
POINTCLOUD_SPATIAL_DATA_SUBDIRECTORY = SPATIAL_DATA_SUBDIRECTORY / 'pointcloud'

# Logs

LOGS_DIRECTORY = PROJECT_DIRECTORY / 'logs'

REQUIRED_PATHS = [
    PYTHON_DIRECTORY,
    PROJECT_DIRECTORY,
    DATA_DIRECTORY,
    SPATIAL_DATA_SUBDIRECTORY,
    TABULAR_DATA_SUBDIRECTORY,
    VECTOR_SPATIAL_DATA_SUBDIRECTORY,
    RASTER_SPATIAL_DATA_SUBDIRECTORY,
    POINTCLOUD_SPATIAL_DATA_SUBDIRECTORY,
    LOGS_DIRECTORY,
]

GADM_URL = "https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-levels.zip"