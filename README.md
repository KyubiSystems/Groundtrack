Groundtrack
===========

Calculate and display realtime satellite groundtracks on HTML5 map. 

Input TLE (Two-Line Element Set) as JSON file. Python script calculates subsatellite ground track for past 60 minutes, returns JSON set of lat,long tuples. HTML5/Javascript calls Python script via AJAX, updates plot on world map.

OPTION: Access SpaceTrack.org and automatically grab latest TLE.

OPTION: Notification of satellite rising above observer's horizon.

OPTION: Control of steerable antenna via JSON-RPC/XML-RPC.