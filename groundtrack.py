#!/usr/bin/env python

# Modified from PLAN-13 Satellite Position Calculation Program
# PLAN-13 by James Miller G3RUH, AMSAT UK

import json

from math import radians, degrees, cos, sin, sqrt, abs
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

# Convert satellite epoch to Day Number and fraction of day
DE = fnDay(YE, 1, 0) + int(TE)
TE = TE - int(TE)

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
TEG  = (DE - fnDay(YG, 1, 0)) + TE   # Elapsed Time: Epoch - YG
GHAE = radians(G0) + TEG*WE          # GHA Aries, epoch
MRSE = radians(G0) + TEG*WW + PI     # Mean RA of Sun at Sat epoch
MASE = radians(MAS0 + MASD * TEG)    # Mean MA of Sun at Sat epoch 

# Antenna unit vector in orbit plane coordinates

aLong = TLE['aLong']
aLat = TLE['aLat']

ANvec = [ -cos(radians(aLat)) * cos(radians(aLong)),
          -cos(radians(aLat)) * sin(radians(aLong)),
          -sin(radians(aLat)) ]

# Calculate Satellite position at Day DN, Time TN

def satVector():
    T   = (DN - DE) + (TN - TE)      # Elapsed T since epoch, days
    DT  = DC * T/2                   # Linear drag terms
    KD  = 1 + 4*DT                   # ...
    KDP = 1 - 7*DT                   # ...

    M = MA + MM*T * (1 - 3*DT)       # Mean anomaly at YR, TN
    DR = int( M / (2*PI) )           # Strip out whole number of revs
    M = M - DR*2*PI                  # M now in range 0 - 2pi
    RN = RV + DR                     # Current Orbit Number

# Solve M = EA - EC*sin(EA) for EA given M, by Newton's method

    EA = M                           # Initial solution
    converged = False
    while not converged:
        C = cos(EA)
        S = sin(EA)
        DNOM = 1 - EC*C
        D = (EA - EC*S - M)/DNOM
        EA = EA - D
        converged = (abs(D) < 1e-5)

    A = A0 * KD
    B = B0 * KD
    RS = A * DNOM

# Calculate satellite position in plane of ellipse
    Svec = [ A * (C-EC),
             B * S ]

    Vvec = [ -A * S / (DNOM * N0),
              B * C / (DNOM * N0) ]

# Plane->celestial coordinate transformations, [C] = [RAAN] * [IN] * [AP]

# Compute SATellite's position vector, ANTenna axis unit vector
# and velocity in CELESTIAL coordinates (Note: Sz=0, Vz=0)

# Also express SAT, ANT and VEL in geocentric coordinates


# ----------------------------------------
# Calculate Sun unit vector

def sunVector():
    pass
# ----------------------------------------
# Calculate range/velocity/antenna vectors 

def rangeVector():
    pass

# ----------------------------------------
# Convert day-number to date; valid 1900 Mar 01 - 2100 Feb 28

def fnDate():
    pass

# ----------------------------------------
# Convert date to day-number

def fnDay():
    pass

# ----------------------------------------
# Compute satellite footprint on Earth

def satFoot():
    pass

# Take satellite distance, sub-satellite lat/long and compute unit vectors'
# x,y,z of N points of footprint on Earth's surface in Geocentric coordinates
# Also terrestrial latitude, longitude of points



