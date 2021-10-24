'use strict';

const margin = {top: 50, right: 10, bottom: 10, left: 10},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom,
      color = d3.scaleOrdinal().range(d3["schemeCategory20"]);

const treemap = d3.treemap().size([width, height]);

const div = d3.select("body").append("div")
    .style("position", "relative")
    .style("width", (width + margin.left + margin.right) + "px")
    .style("height", (height + margin.top + margin.bottom) + "px")
    .style("left", margin.left + "px")
    .style("top", margin.top + "px");


d3.json("../../Data/Sickle/AH_Sickle_Cell_Disease_Provisional_Death_Counts_2019-2021-race-modified.json", function(error, data) {
  if (error) throw error;

  var root = d3.hierarchy(data.race, (d) => d.children)
    .sum((d) => d.scd); //Had to add 1 since the scd values are 0 for many

  const tree = treemap(root);
  
  var value = (d) => {return d.scd}; 
  var heir = "race";

  const node = div.datum(root).selectAll(".node")
      .data(tree.leaves())
    .enter().append("div")
      .attr("class", "node")
      .style("left", (d) => d.x0 + "px")
      .style("top", (d) => d.y0 + "px")
      .style("width", (d) => Math.max(0, d.x1 - d.x0 - 1) + "px")
      .style("height", (d) => Math.max(0, d.y1 - d.y0  - 1) + "px")
      .style("background", (d) => color(d.parent.data.name))
      .text((d) => d.data.name);

  d3.selectAll(".form-top input").on("change", function change() {
    
    if(this.value==="race")
    {
        heir = "race";
        root = d3.hierarchy(data.race, (d) => d.children)
        .sum(value);
    }
    else if(this.value === "age")
    {
        heir = "age";
        root = d3.hierarchy(data.age, (d) => d.children)
        .sum(value);
    }
    else
    {
        heir = "quarter";
        root = d3.hierarchy(data.quarter, (d) => d.children)
        .sum(value);          
    } 
    node.data(treemap(root).leaves())
        .transition()
            .duration(1500)
            .style("left", (d) => d.x0 + "px")
            .style("top", (d) => d.y0 + "px")
            .style("width", (d) => Math.max(0, d.x1 - d.x0 - 1) + "px")
            .style("height", (d) => Math.max(0, d.y1 - d.y0  - 1) + "px")
            .style("background", (d) => color(d.parent.data.name))
            .text((d) => d.data.name);
  });

  d3.selectAll(".form-bottom input").on("change", function change(){
    
    if(this.value === "scd")
    {
        value = (d) => {return d.scd};
    }
    else if(this.value === "scd_underlying")
    {
        value = (d) => {return d.scd_underlying};
    }
    else 
    {
        value = (d) => {return d.scd_multi};
    }

    if(heir === "race")
    {
        root = d3.hierarchy(data.race, (d) => d.children)
        .sum(value);
    }
    else if(heir === "age")
    {
        root = d3.hierarchy(data.age, (d) => d.children)
        .sum(value);
    }
    else
    {
        root = d3.hierarchy(data.quarter, (d) => d.children)
        .sum(value);
    }
    node.data(treemap(root).leaves())
        .transition()
            .duration(1500)
            .style("left", (d) => d.x0 + "px")
            .style("top", (d) => d.y0 + "px")
            .style("width", (d) => Math.max(0, d.x1 - d.x0 - 1) + "px")
            .style("height", (d) => Math.max(0, d.y1 - d.y0  - 1) + "px")
            .style("background", (d) => color(d.parent.data.name))
            .text((d) => d.data.name);
  });
});