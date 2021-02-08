import os

here = os.path.dirname(__file__)

if os.path.exists(os.path.join(here, './newrelic-pygeoapi.ini')):
    import newrelic.agent
    newrelic.agent.initialize(os.path.join(here, './newrelic-pygeoapi.ini'))

os.environ['PYGEOAPI_CONFIG'] = os.path.join(here, './conf/msc-geomet-pygeoapi-config.yml')
os.environ['PYGEOAPI_OPENAPI'] = os.path.join(here, './conf/msc-geomet-pygeoapi-openapi.yml')

from pygeoapi.flask_app import APP as application
