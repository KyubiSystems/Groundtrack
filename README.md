Groundtrack
===========

**Calculate and display realtime satellite groundtracks on HTML5 map.**

(http://www.tigris.org.uk/images/groundtrack.png "Example output")

Input TLE (Two-Line Element Set) from file or online archive. Python script calculates subsatellite ground track for past 60 minutes, returns JSON set of lat,long tuples. HTML5/Javascript calls Python script via AJAX, updates SVG plot on world map.

**Don't use this for anything serious at the moment. The results are horribly wrong.**

TODO
----

* Unwrong it.
* Prettier graphics, SVG animation
* Access Celestrak (or other archive) and automatically grab latest TLE.
* Notification of satellite rising above observer's horizon.
* Control of steerable antenna via JSON-RPC/XML-RPC.
