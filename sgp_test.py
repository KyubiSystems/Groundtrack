from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

from math import atan2, cos, pi, sin, sqrt, tan
from datetime import datetime

from sidereal import utcDatetime2gmst, ymd2jd

# twoline2rv() function returns a Satellite object whose attributes
# carry the data loaded from the TLE entry

# Satellite attributes of interest
# satnum     -  Unique satellite number given in the TLE file
# epochyr    - Full four-digit year of this element set's epoch moment
# epochdays  - Fractional days into the year of the epoch moment
# jdsatepoch - Julian date of the epoch (computed from epochyr and epochdays)
# ndot       - First time derivative of the mean motion (ignored by SGP4)
# nddot      - Second time derivative of the mean motion (ignored by SGP4)
# bstar      - Ballistic drag coefficient B* in inverse earth radii
# inclo      - Inclination in radians
# nodeo      - Right ascension of ascending node in radians
# ecco       - Eccentricity
# argpo      - Argument of perigee in radians
# mo         - Mean anomaly in radians
# no         - Mean motion in radians per minute

# Calculate groundtrack
def groundtrack(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]

    # Constants for WGS-87 ellipsoid
    a = 6378.137
    e = 8.1819190842622e-2

    # Groundtrack
    b = sqrt(pow(a,2) * (1-pow(e,2)))
    ep = sqrt((pow(a,2)-pow(b,2))/pow(b,2))
    p = sqrt(pow(x,2)+pow(y,2))
    th = atan2(a*z, b*p)
    lon = atan2(y, x)
    lat = atan2((z+ep*ep*b*pow(sin(th),3)), (p-e*e*a*pow(cos(th),3)))
    n = a/sqrt(1-e*e*pow(sin(lat),2))

    alt = p/cos(lat)-n
    lat = (lat*180)/pi
    lon = (lon*180)/pi

    return (lat, lon, alt)

# Test TLE for Hubble Space Telescope
line1 = ('1 20580U 90037B   14101.16170949  '
         '.00002879  00000-0  18535-3 0  4781')
line2 = ('2 20580 028.4694 117.6639 0002957 '
         '290.9180 143.6730 15.05140277114603')

satellite = twoline2rv(line1, line2, wgs72)

date = datetime(2000, 6, 29, 12, 46, 19)

position, velocity = satellite.propagate(date.year, date.month, date.day, date.hour, date.minute, date.second)

print position

print velocity

lat, gmra, alt = groundtrack(position)

print str(lat)
print str(gmra)
print str(alt)

gmst = utcDatetime2gmst(date)

print date.timetuple()
print gmst

lon = (gmst * 15.0) - gmra

lonraw = lon
lon = ((lon + 180.0) % 360.0) - 180.0

print lonraw
print lon

