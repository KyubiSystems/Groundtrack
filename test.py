#!/usr/bin/env python

import json

f = open('./TLE.json','r')
TLE = f.read()
f.close()

decoded = json.loads(TLE)

print decoded['epochTime']
print decoded['decayRate']

f = open('./Observer.json','r')
Observer = f.read()
f.close()

decoded2 = json.loads(Observer)

print decoded2['obsLatitude']


