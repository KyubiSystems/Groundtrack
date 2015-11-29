<!DOCTYPE html>
<head>
<meta charset="utf-8">
<style>

body {
 background-color: #000;
}

.land {
  fill: none;
  stroke: #8b8;
  stroke-width: 2;
}

.country-border {
  fill: none;
  stroke: #aca;
}

.satellite {
  fill: none;
  stroke: #f00;
  stroke-width: 2;
}

.text-label {
  fill: #fcc;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 15px;
  font-weight: 200;
}

.now {
  fill: #faa;
}

</style>
<title>Groundtrack: World Map</title>
</head>
<body>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/topojson.v1.min.js"></script>
<script>

var width = 1600,
    height = 900;

var path = d3.geo.path()
    .projection(cylindrical(width, height));

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("./data/world-50m.json", function(error, world) {
  svg.append("path")
      .datum(topojson.feature(world, world.objects.land))
      .attr("class", "land")
      .attr("d", path);

  svg.append("path")
      .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
      .attr("class", "country-border")
      .attr("d", path);
});

function cylindrical(width, height) {
  return d3.geo.projection(function(λ, φ) { return [λ, φ * 2 / width * height]; })
      .scale(width / 2 / Math.PI)
      .translate([width / 2, height / 2]);
}

d3.json("/trackdata", function(error, track) {

  point = {type: "Point", coordinates: track.coordinates[0]}

  console.log(point);
  console.log(track);

  console.log(cylindrical(width, height));

  svg.selectAll(".satellite")
     .data([track])
     .enter()
     .append("path")
     .attr("d", path)
     .attr("class", "satellite");

  svg.selectAll(".now")
     .data([point])
     .enter()
     .append("path")
     .attr("d", path)
     .attr("r", 5)
     .attr("class","now");

  svg.selectAll(".text-label")
     .data([point])
     .enter()
     .append("text")
     .attr("class","text-label")
//     .attr("transform", "translate(" + projection(point.coordinates[0], point.coordinates[1]) + ")";)
     .attr("x", 180)
     .attr("y", 420)
//     .attr("d", path)
     .text('HST');

});

</script>
