#!/usr/bin/env python

def readConfig(filename):

    import json

    f = open('./config/'+filename,'r')
    FILE = f.read()
    f.close()

    JSON = json.loads(FILE)
    return JSON
