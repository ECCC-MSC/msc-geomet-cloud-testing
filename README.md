# msc-geomet-cloud-testing

## Install software

```bash

# install Elasticsearch (latest 7.x) from https://www.elastic.co/downloads/elasticsearch

# install Apache2 (2.4.29)
apt-get install apache2 apache2-bin apache2-utils apache2-data libapache2-mod-wsgi-py3

# generate 
htpasswd -c es-auth.htpasswd admin

# pygeoapi
git clone https://github.com/geopython/pygeoapi.git
pip install -r requirements-provider.txt
python setup.py install

# msc-pygeoapi
git clone https://github.com/ECCC-MSC/msc-pygeoapi.git
python setup.py install

# MapProxy
git clone https://github.com/piensa/mapproxy.git -b dimensions
cd mapproxy
python setup.py install

# MetPX
pip install metpx-sarracenia
```

## Load and configure data

```bash
# load latest MSC HYDAT archive into Elasticsearch
curl -O https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/Hydat_sqlite3_20201104.zip
unzip Hydat_sqlite3_20201104.zip
msc-pygeoapi data hydat add --db=./Hydat.sqlite3 --dataset=all --es=ES_URL --username=admin --password=xxx  # ~6 hours

# edit MetPX configuration
vi deploy/conf/msc-geomet-metpx-config.conf  # edit directory setting accordingly

# subscribe to MSC Datamart MetPX/AMQP feed and pull down a GDPS model run
# runs are daily at 00h and 12h
# the subscription downloads temperature variables in GRIB2
sr_subscribe foreground deploy/conf/msc-geomet-metpx-config.conf

# update pygeoapi configuration
vi deploy/conf/msc-geomet-pygeoapi-config.yml
# update server.bind.host, server.bind.port, server.url
# edit path to a single GDPS file (currently tests/data/GRIB2_FILENAME.grib2)
# edit host and port of ES setting for HYDAT collection (currently http://localhost:9200)

# generate pygeoapi OpenAPI document
pygeoapi generate-openapi-document -c deploy/conf/msc-geomet-pygeoapi-config.yml > deploy/conf/msc-geomet-pygeoapi-openapi.yml
```

## Deploy

```bash
vi deploy/apache2/msc-geomet-cloud-testing.conf
# adjust paths to .wsgi scripts

apache2 start

curl http://host:port/pygeoapi/  # OGC API landing page
curl http://host:port/mapproxy/  # HTML page
```
