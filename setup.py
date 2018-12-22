#!/usr/bin/env python

from bottle import route, run, static_file, template
from orbitdata import geojson
from config import APP_PATH

# Returns GeoJSON line segment for satellite groundtrack
@route('/trackdata')
def trackdata():
    groundtrack = geojson()
    return groundtrack

# Helper function to return path to static file
@route('/data/<filename>')
def server_static(filename):
    STATIC_PATH = APP_PATH + 'data'
    return static_file(filename, root=STATIC_PATH)

# Main template to render world map
# Map template stored in ./views/map_template.tpl
@route('/worldmap')
def worldmap():
    return template('map_template')

run(host='localhost', port=8081, debug=True)
