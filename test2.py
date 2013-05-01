#!/usr/bin/env python

# Modified from PLAN-13 Satellite Position Calculation Program
# PLAN-13 by James Miller G3RUH, AMSAT UK

import json

from math import radians, degrees, cos, sin, sqrt
from math import pi as PI
from datetime import datetime, timedelta

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

(X, Y, Z) = (0, 1, 2) # ordinal type for axes X, Y, Z

# Calculate position of observer
obsLat = radians(Observer['obsLatitude'])
obsLong = radians(Observer['obsLongitude'])
obsHeight = Observer['ObsHeight']/1000.0

# WGS-84 Earth ellipsoid
rE = 6378.137     # radius of Earth
fE = 1/298.257224 # polar flattening of Earth

Rx = (rE ** 2)/(sqrt((rE**2) * cos(obsLat)**2)) + obsHeight
Rz = (rE - (1 - fE))**2 / sqrt(rE**2 * cos(obsLat)**2) + obsHeight

# Observer's unit vectors UP, EAST and NORTH in GEOCENTRIC coords
Uvec = [ cos(obsLat) * cos(obsLong),
         cos(obsLat) * sin(obsLong),
         sin(obsLat) ]

Evec = [ -sin(obsLong),
          cos(obsLong),
          0 ]

Nvec = [ -sin(obsLat) * cos(obsLong),
         -sin(obsLat) * sin(obsLong),
          cos(obsLat) ]

# Observer's XYZ coords at Earth's surface
Ovec = [ Rx * Uvec[X],
         Rx * Uvec[Y],
         Rz * Uvec[Z] ]

# Convert input satellite angles to radians
RAAN = radians(TLE['RAAN'])
Incl = radians(TLE['Inclination'])
argPeri = radians(TLE['argPerigee'])
meanAnom = radians(TLE['meanAnomaly'])

meanMotion = TLE['meanMotion']
decayRate = TLE['decayRate']

# Date parameters
meanYear = 365.25
tropicalYear = 365.2421874
rotationRate = 2 * PI / tropicalYear

We = 2 * PI + rotationRate
W0 = We / 86400 # rotation in radians/sec

# Observer's velocity in GEOCENTRIC coords
VOvec = [ -Ovec[Y] * W0,
           Ovec[X] * W0,
           0 ]

# Convert satellite epoch to Day Number


# Average precession rates
GM = 3.986E5                  # Earth's Gravitational Constant km^3/s^2
J2 = 1.08263E-3               # 2nd Zonal Coeff, Earth's Gravity Field
N0 = meanMotion / 86400       # Mean motion, rad/s
A0 = (GM/N0/N0) ** (1/3)      # Semi-major axis, km
B0 = A0 * sqrt(1 - Ecc * Ecc) # Semi-minor axis, km





