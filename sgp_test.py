from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

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

# Test TLE for Hubble Space Telescope
line1 = ('1 20580U 90037B   14101.16170949  '
         '.00002879  00000-0  18535-3 0  4781')
line2 = ('2 20580 028.4694 117.6639 0002957 '
         '290.9180 143.6730 15.05140277114603')

satellite = twoline2rv(line1, line2, wgs72)

position, velocity = satellite.propagate(2000, 6, 29, 12, 50, 19)

print position

print velocity

