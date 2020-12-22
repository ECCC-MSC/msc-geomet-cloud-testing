import os

os.environ['PYGEOAPI_CONFIG'] = './conf/msc-geomet-pygeoapi-config.yml'
os.environ['PYGEOAPI_OPENAPI'] = './conf/msc-geomet-pygeoapi-openapi.yml'

from pygeoapi.flask_app import APP as application
