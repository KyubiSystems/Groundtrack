<!DOCTYPE html>
<meta charset="utf-8">
<style>

body {
 background-color: #000;
}

.land {
  fill: #696;
}

.country-border {
  fill: none;
  stroke: #aca;
}

.satellite {
  fill: none;
  stroke: #f00;
}

.now {
  fill: #f00;
}

</style>
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

  svg.selectAll(".geojson")
     .data([point])
     .enter()
     .append("path")
     .attr("d", path)
     .attr("r", 5)
     .attr("class","now");

  svg.selectAll(".geojson")
     .data([track])
     .enter()
     .append("path")
     .attr("d", path)
     .attr("class", "satellite");

});

</script>
