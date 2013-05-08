#!/usr/bin/env python

# Modified from PLAN-13 Satellite Position Calculation Program
# PLAN-13 by James Miller G3RUH, AMSAT UK

import json

from math import radians, degrees, cos, sin, sqrt
from math import pi as PI
from datetime import datetime, timedelta

from file_utils import readConfig

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
RAAN = radians(TLE['RAAN'])             # Right Acension of Ascending Node (RAAN)
Incl = radians(TLE['Inclination'])      # Inclination
argPeri = radians(TLE['argPerigee'])    # Argument of Perigee
meanAnom = radians(TLE['meanAnomaly'])  # Mean anomaly

meanMotion = TLE['meanMotion'] * 2 * PI # Mean motion
decayRate = TLE['decayRate'] * 2 * PI   # Decay Rate

# Date parameters
meanYear = 365.25
tropicalYear = 365.2421874
rotationRate = 2 * PI / tropicalYear

We = 2 * PI + rotationRate    # rotation in radians/day
W0 = We / 86400               # rotation in radians/sec

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
PC = rEarth * A0 / (B0 * B0)  # Precession constant, radians/day
QD = -PC * cos(Incl)          # Node precession rate, radians/day
WD = PC * ( 5 * cos(Incl) * cos(Incl) - 1 ) / 2 # Perigee precession rate, radians/day
DC = -2 * decayRate / meanMotion / 3 # Drag coefficient (ang momentum rate)/(ang momentum) s^-1

# Sidereal and solar data. NEVER needs changing. Valid to year ~2015 (hmmm...)
YG = 2000
G0 = 98.9821                  # Greenwich Hour Angle Aries, year YG, Jan 0.0
MAS0 = 356.0507               # Mean anonaly Sun (deg)
MASD = 0.98560028             # Mean anomaly Sun rate (deg/day)
INS = radians(23.4393)        # Solar inclination
EQC1 = 0.03342                # Sun's equation of centre terms
EQC2 = 0.00035                # Sun's equation of centre terms

# Bring Sun data to satellite epoch

# Antenna unit vector in orbit plane coordinates

aLong = TLE['aLong']
aLat = TLE['aLat']

ANvec = [ -cos(radians(aLat)) * cos(radians(aLong)),
          -cos(radians(aLat)) * sin(radians(aLong)),
          -sin(radians(aLat)) ]

# Calculate Satellite position at Day DN, Time TN

def satVector():

# Calculate Sun unit vector

def sunVector():

# Calculate range/velocity/antenna vectors 

def rangeVector():

