function WeatherSource() {
    fetch("https://api.openweathermap.org/data/2.5/weather?q=Munich&units=metric&appid=99b9922597ba486ef77f40305e0beab6").then((response) => response.json()).then((user) => {
        let temp = user.main.temp;
        let feels_like = user.main.feels_like;
        let wind = user.wind.speed;
        let desc = user.weather[0]["description"];
        document.getElementById("temp2").innerHTML = "Temp: "+ temp +' °C';
        document.getElementById("feels").innerHTML = "Feeling Like: "+feels_like +' °C';
        document.getElementById("wind").innerHTML = "Wind Speed: "+wind +' m/s';
        document.getElementById("desc2").innerHTML = "Description: "+desc;
      });
}

const targetDiv = document.getElementById("weather");
const btn = document.getElementById("temp22");
btn.onclick = function () {
  WeatherSource()
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
};

/* Map code starts */

// The svg
var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

// Map and projection
var projection = d3.geoMercator()
    .center([2, 47])                // GPS of location to zoom on
    .scale(1020)                       // This is like the zoom
    .translate([ width/2, height/2 ])

// Create data for circles:
var markers = [
  {long: 9.083, lat: 42.149, group: "A", size: 34}, // corsica
  {long: 7.26, lat: 43.71, group: "A", size: 14}, // nice
  {long: 2.349, lat: 48.864, group: "B", size: 87}, // Paris
  {long: -1.397, lat: 43.664, group: "B", size: 41}, // Hossegor
  {long: 3.075, lat: 50.640, group: "C", size: 78}, // Lille
  {long: -3.83, lat: 48, group: "C", size: 12} // Morlaix
];

// Load external data and boot
d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson", function(data){

    // Filter data
    data.features = data.features.filter( function(d){return d.properties.name=="France"} )

    // Create a color scale
    var color = d3.scaleOrdinal()
      .domain(["A", "B", "C" ])
      .range([ "#402D54", "#D18975", "#8FD175"])

    // Add a scale for bubble size
    var size = d3.scaleLinear()
      .domain([1,100])  // What's in the data
      .range([ 4, 50])  // Size in pixel

    // Draw the map
    svg.append("g")
        .selectAll("path")
        .data(data.features)
        .enter()
        .append("path")
          .attr("fill", "#b8b8b8")
          .attr("d", d3.geoPath()
              .projection(projection)
          )
        .style("stroke", "black")
        .style("opacity", .3)

    // Add circles:
    svg
      .selectAll("myCircles")
      .data(markers)
      .enter()
      .append("circle")
        .attr("class" , function(d){ return d.group })
        .attr("cx", function(d){ return projection([d.long, d.lat])[0] })
        .attr("cy", function(d){ return projection([d.long, d.lat])[1] })
        .attr("r", function(d){ return size(d.size) })
        .style("fill", function(d){ return color(d.group) })
        .attr("stroke", function(d){ return color(d.group) })
        .attr("stroke-width", 3)
        .attr("fill-opacity", .4)


    // This function is gonna change the opacity and size of selected and unselected circles
    function update(){

      // For each check box:
      d3.selectAll(".checkbox").each(function(d){
        cb = d3.select(this);
        grp = cb.property("value")

        // If the box is check, I show the group
        if(cb.property("checked")){
          svg.selectAll("."+grp).transition().duration(1000).style("opacity", 1).attr("r", function(d){ return size(d.size) })

        // Otherwise I hide it
        }else{
          svg.selectAll("."+grp).transition().duration(1000).style("opacity", 0).attr("r", 0)
        }
      })
    }

    // When a button change, I run the update function
    d3.selectAll(".checkbox").on("change",update);

    // And I initialize it at the beginning
    update()
})



/* Graph code starts */

// create an array with nodes
var nodes = new vis.DataSet([
    {id: 1, value: 20, label: '1'},
    {id: 2, value: 5, label: '2'},
    {id: 3, value: 10, label: '3'},
    {id: 4, value: 15, label: '4'},
    {id: 5, value: 8, label: '5'},
    {id: 6, value: 10, label: '6'},
    {id: 7, value: 50, label: '7'},
    {id: 8, value: 10, label: '8'},
    {id: 9, value: 10, label: '9'},
    {id: 10, value: 10, label: '10'},
    {id: 11, value: 10, label: '11'},
    {id: 12, value: 4, label: '12'},
    {id: 13, value: 2, label: '13'},
    {id: 14, value: 1, label: '14'}
  ]);

  // create an array with edges
  var edges = new vis.DataSet([
    {from: 1, to: 2},
    {from: 1, to: 4},
    {from: 1, to: 5},
    {from: 2, to: 6},
    {from: 2, to: 7},
    {from: 2, to: 8},
    {from: 3, to: 9},
    {from: 3, to: 10},
    {from: 3, to: 11},
    {from: 10, to: 12},
    {from: 10, to: 13},
    {from: 10, to: 14},
    {from: 7, to: 11},
    {from: 8, to: 14},
    {from: 11, to: 12},
    {from: 5, to: 9}
  ]);

  // create a network
  var container = document.getElementById('mynetwork');

  // provide the data in the vis format
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
    nodes: {
      autoResize: true,
      height: '100%',
      width: '100%',
      shape: 'circle',
      font: {
        size: 30
      },
      scaling:{
        label: {
          min:8,
          max:50
        }
      },
      borderWidth: 1,
      shadow: true,
      margin: {
        top: 10,
        left: 20,
        right: 20,
        bottom: 10
      },
      color: {
        border: "",
        background: "#b2dfdb",
        highlight : {
          border: '#e57373',
          background: '#ffcdd2'
        }
      }
    },
    layout: {
      improvedLayout: true,
      hierarchical: {
        enabled: false,
        direction: 'UD',
        sortMethod: 'hubsize',
        parentCentralization: true,
        blockShifting: true,
        edgeMinimization: true
      }
    },
    edges: {
      smooth: true,
      chosen: true,
      arrows: {
        to : {
          enabled: true,
          type: 'arrow'
        }
      },
      color: {
        color: "#b2dfdb",
        highlight:'#ffcdd2',
        hover: '#848484',
        inherit: 'from',
        opacity:1.0
      },
    }
  };

  // initialize your network!
  var network = new vis.Network(container, data, options);

  network.on("initRedraw", function () {
    // do something like move some custom elements?
  });
  network.on("beforeDrawing", function (ctx) {

  });
  network.on("afterDrawing", function (ctx) {
    //var nodeId = 1;
    //var nodePosition = network.getPositions([nodeId]);
    //roundRect(ctx, nodePosition[nodeId].x-70, nodePosition[nodeId].y-70, 150, 120, 40, true);

  });

  function roundRect(ctx, x, y, width, height, radius, fill, stroke) {
    if (typeof stroke == 'undefined') {
      stroke = true;
    }
    if (typeof radius === 'undefined') {
      radius = 5;
    }
    if (typeof radius === 'number') {
      radius = {tl: radius, tr: radius, br: radius, bl: radius};
    } else {
      var defaultRadius = {tl: 0, tr: 0, br: 0, bl: 0};
      for (var side in defaultRadius) {
        radius[side] = radius[side] || defaultRadius[side];
      }
    }
    ctx.beginPath();
    ctx.moveTo(x + radius.tl, y);
    ctx.lineTo(x + width - radius.tr, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius.tr);
    ctx.lineTo(x + width, y + height - radius.br);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius.br, y + height);
    ctx.lineTo(x + radius.bl, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius.bl);
    ctx.lineTo(x, y + radius.tl);
    ctx.quadraticCurveTo(x, y, x + radius.tl, y);
    ctx.closePath();
    if (fill) {
      ctx.fill();
    }
    if (stroke) {
      ctx.stroke();
    }

    ctx.strokeText("AAA",x,y);
  }



  /* Animate Credit Card */

  gsap.timeline()
    .set('.logo',     { x:215, y:482 })
    .set('.chip',     { x:148, y:66 })
    .set('.knot',     { x:22, y:250 })
    .set('.numTxt',   { x:22, y:375 })
    .set('.nameTxt',  { x:22, y:410 })
    .add(centerMain(), 0.2)
    .from('.ball',    { duration:2,
                        transformOrigin:'50% 50%',
                        scale:0,
                        opacity:0,
                        ease:'elastic',
                        stagger:0.2
                      }, 0)
    .fromTo('.card2',  { x:200,
                        y:40,
                        transformOrigin:'50% 50%',
                        rotation:-4,
                        skewX:10,
                        skewY:4,
                        scale:2,
                        opacity:0
                      },{
                        duration:1.3,
                        skewX:0,
                        skewY:0,
                        scale:1,
                        opacity:1,
                        ease:'power4.inOut'
                      }, 0.2)
        


function centerMain(){ gsap.set('.main', {x:'50%', xPercent:-50, y:'50%', yPercent:-50}); }
window.onresize = centerMain;

window.onmousemove = (e)=> {
  let winPercent = { x:e.clientX/window.innerWidth, y:e.clientY/window.innerHeight },
      distFromCenter = 1 - Math.abs((e.clientX - window.innerWidth/2)/window.innerWidth*2);
  
  gsap.timeline({defaults:{duration:0.5, overwrite:'auto'}})
      .to('.card2',        {rotation:-7+9*winPercent.x}, 0)
      .to('.fillLight',   {opacity:distFromCenter}, 0)  
      .to('.bg',          {x:100-200*winPercent.x, y:20-40*winPercent.y}, 0) 
}
 




