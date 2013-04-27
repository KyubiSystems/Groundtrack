#!/usr/bin/env python

import json

def readConfig(filename):
    f = open('./config/'+filename,'r')
    FILE = f.read()
    f.close()
    
    JSON = json.loads(FILE)
    return JSON

TLE = readConfig('TLE.json')
print TLE['epochTime']
print TLE['decayRate']

Observer = readConfig('Observer.json')
print Observer['obsLatitude']
