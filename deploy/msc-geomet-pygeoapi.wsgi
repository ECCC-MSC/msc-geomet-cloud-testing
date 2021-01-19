import os

here = os.path.dirname(__file__)

os.environ['PYGEOAPI_CONFIG'] = os.path.join(here, './conf/msc-geomet-pygeoapi-config.yml')
os.environ['PYGEOAPI_OPENAPI'] = os.path.join(here, './conf/msc-geomet-pygeoapi-openapi.yml')

from pygeoapi.flask_app import APP as application
