Groundtrack
===========

**Calculate and display realtime satellite groundtracks on HTML5 map.**

<img src="http://www.tigris.org.uk/images/groundtrack.jpg" width=450>

Input TLE (Two-Line Element Set) as JSON file. Python script calculates subsatellite ground track for past 60 minutes, returns JSON set of lat,long tuples. HTML5/Javascript calls Python script via AJAX, updates plot on world map.

Options:
--------
* Access SpaceTrack.org and automatically grab latest TLE.
* Notification of satellite rising above observer's horizon.
* Control of steerable antenna via JSON-RPC/XML-RPC.