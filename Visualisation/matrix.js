
// set the dimensions and margins of the graph
var margin = {top: 80, right: 25, bottom: 30, left: 40},
  width = screen.width - margin.left - margin.right,
  height = screen.height - margin.top - margin.bottom;


// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

var coord = document.querySelector('#info');
var cd = document.createTextNode("");
coord.appendChild(cd);

d3.csv("../Data/bio-diseasome/bio-diseasome-modified-matrix.csv", function(data) {

  var Xval = d3.map(data, function(d){return d.xval;}).keys()
  var Yval = d3.map(data, function(d){return d.yval;}).keys()

  // Build X scales and axis:
  var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(Xval)
    .padding(0.05);
  svg.append("g")
    .style("font-size", 2)
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSize(0))
    .select(".domain").remove()

  // Build Y scales and axis:
  var y = d3.scaleBand()
    .range([ height, 0 ])
    .domain(Yval)
    .padding(0.05);
  svg.append("g")
    .style("font-size", 2)
    .call(d3.axisLeft(y).tickSize(0))
    .select(".domain").remove()

  // Three function that change the tooltip when user hover / move / leave a cell
  var mouseover = function(d) {
    d3.select(this)
      .style("stroke", "black")
      .style("opacity", 1)
  }
  var mousemove = function(d) {
    cd.nodeValue = d.xval + " " + d.yval;
  }
  var mouseleave = function(d) {
    d3.select(this)
      .style("stroke", "none")
      .style("opacity", 0.8)
  }

  // add the squares
  svg.selectAll()
    .data(data, function(d) {return d.xval+':'+d.yval;})
    .enter()
    .append("rect")
      .attr("x", function(d) { return x(d.xval) })
      .attr("y", function(d) { return y(d.yval) })
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("width", x.bandwidth() )
      .attr("height", y.bandwidth() )
      .style("fill", function(d) { return d.value == 1? 'red':'white'})
      .style("stroke-width", 4)
      .style("stroke", "none")
      .style("opacity", 0.8)
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
})

// Add title to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "left")
        .style("font-size", "22px")
        .text("Adjacency matrix for Network");

// Add subtitle to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -20)
        .attr("text-anchor", "left")
        .style("font-size", "14px")
        .style("fill", "grey")
        .style("max-width", 400)
        .text("The colored boxes denote that an edge exists between the nodes.");

