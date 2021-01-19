import os

here = os.path.dirname(__file__)

from mapproxy.wsgiapp import make_wsgi_app
application = make_wsgi_app(os.path.join(here, './conf/msc-geomet-mapproxy-config.yml'))

