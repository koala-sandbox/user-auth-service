import os

import main as main_module
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import CollectorRegistry, multiprocess
from fastapi import FastAPI

# Iterating through each attribute in the main module
for attr_name in dir(main_module):
    # Getting the attribute
    attr = getattr(main_module, attr_name)
    
    # Checking if the attribute is an instance of FastAPI
    if isinstance(attr, FastAPI):
        appByType = attr
        break
# In case you need Prometheus exporter to run run multi process don't forget to set up environment variable for Prometheus multi-process directory
# PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus_multiproc

PROMETHEUS_MULTIPROC_DIR = 'PROMETHEUS_MULTIPROC_DIR'

def create_folder_if_not_exists(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Metrics folder '{path}' created successfully.")
    except OSError as error:
        print(f"Metrics folder cannot be created because of the following error: {error}")

if os.getenv(PROMETHEUS_MULTIPROC_DIR) is not None:
    print(f"Environment variable {PROMETHEUS_MULTIPROC_DIR} is defined running metrics collection multiprocess mode.")
    create_folder_if_not_exists(os.getenv(PROMETHEUS_MULTIPROC_DIR))
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)

    # Instrument the app
    instrumentator = Instrumentator(registry=registry)  # Pass the custom registry
    instrumentator.instrument(appByType).expose(appByType) 
else:
    print(f"Environment variable {PROMETHEUS_MULTIPROC_DIR} is not defined running metrics colletion in single process mode.")
    instrumentator = Instrumentator()
    instrumentator.instrument(appByType).expose(appByType) 