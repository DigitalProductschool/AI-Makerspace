
map.on('click', (e) => {
  // Set `bbox` as 5px reactangle area around clicked point.
  const bbox = [
  [e.point.x - 5, e.point.y - 5],
  [e.point.x + 5, e.point.y + 5]
  ];
  // Find features intersecting the bounding box.
  const selectedFeatures = map.queryRenderedFeatures(bbox, {
  layers: ['points2','points3','points4']
  });

  if(selectedFeatures.length > 0){

    const fips = selectedFeatures.map(
      (feature) => feature.properties
      );

      var avgdur = JSON.parse(fips[0].stop)["avgDuration"];
      var maxdur = JSON.parse(fips[0].stop)["maxDuration"];
      var mindur = JSON.parse(fips[0].stop)["minDuration"];
      var addressdata = JSON.parse(fips[0].address)["street"];
      var districtdata = JSON.parse(fips[0].address)["district"];
    
      var row2 = JSON.parse(fips[0].lane)["row2"];
      var radweg = JSON.parse(fips[0].lane)["radweg"];
      var burgersteig = JSON.parse(fips[0].lane)["burgersteig"];
      var regular = JSON.parse(fips[0].lane)["regular"];
      var undefined = JSON.parse(fips[0].lane)["undefinedrow"];
      var totalcar = JSON.parse(fips[0].lane)["noOfVehicles"];
    
      var theDivexpand = document.getElementById("demo3");
      if (screen.width < 700){
        theDivexpand.style.height = "16rem";
      }
      else{
        theDivexpand.style.height = "22rem";
      }
      var theDiv2 = document.getElementById("graphing");
      const content2 = document.createTextNode("Avg Parkzeit: "+avgdur);
      const content3 = document.createTextNode("Max Parkzeit: "+maxdur);
      const content4 = document.createTextNode("Min Parkzeit: "+mindur);
      const content5 = document.createTextNode("Address: "+addressdata+', '+districtdata);
      if(document.getElementById('clicktext') !== null){
        var el = document.getElementById('clicktext');
        el.parentNode.removeChild(el);
      }
      if(document.getElementById('pointdetails') !== null){
        var el2 = document.getElementById('pointdetails');
        el2.parentNode.removeChild(el2);
      }
    
      const head1 = document.createTextNode("Wo ? ");
      var h61 = document.createElement("h6");
      const head2 = document.createTextNode("Wie lange ? ");
      var h62 = document.createElement("h6");
      var br = document.createElement("br");
      var br2 = document.createElement("br");
      var hor1 = document.createElement("hr");
      var hor2 = document.createElement("hr");
      var span = document.createElement('div');
      var chart2 = document.createElement('div');
      chart2.id = "piechart";
      chart2.style.padding = "0px";
      if (screen.width < 700){
        span.style.fontSize = "7px";
      }
      else{
        span.style.fontSize = "12px";
      }
      
      span.style.color = "black";
      span.style.whitespace = "pre";
      span.id = "pointdetails";
    
      h61.appendChild(head1);
      h62.appendChild(head2);
      span.appendChild(h61);
      span.appendChild(content5); 
      span.appendChild(hor1);
      span.appendChild(h62);
      span.appendChild(content2);
      span.appendChild(br);
      span.appendChild(content3);
      span.appendChild(br2);
      span.appendChild(content4); 
      span.appendChild(hor2);
      span.appendChild(chart2);
    
      theDiv2.appendChild(span);
    
    
      // Load Google's charting functions
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      
      // Put the JSON array into a variable
      const json = [
        { "condiment" : "2,-Reihe", "number" : row2 },
        { "condiment" : "Radweg", "number" : radweg },
        { "condiment" : "Regulär", "number" : regular },
        { "condiment" : "Bürgersteig", "number" : burgersteig },
        { "condiment" : "Undefiniert", "number" : undefined }
      ];
      
      // Draw the chart and set the chart values
      function drawChart() {
        
        // Set the columns for the Google Chart in the first line of the array
        var condArray = [['Condiment', 'Number']]; 
        // Loop through the JSON array, set up the value pair & push to the end of condArray
        for(i=0; i<json.length; i++) {
          condArray.push([json[i].condiment, json[i].number]);
        }
       
        // Set the Google Chart options (title, width, height, and colors can be set)
        if (screen.width < 700){
            var options = {
                title: 'Anzahl an Fahrzeugen : '+totalcar,
                'width': 100,
                'height': 50,
                'chartArea': {left:10,top:20, 'width': '100%', 'height': '70%'},
                'colors' : ['#e00c0c', '#2c36e3', '#4f7be4', '#b9b9c0', '#edecf0']
              };
          }
        else{
            var options = {
                title: 'Anzahl an Fahrzeugen : '+totalcar,
                'width': 200,
                'height': 100,
                'chartArea': {left:10,top:20, 'width': '100%', 'height': '70%'},
                'colors' : ['#e00c0c', '#2c36e3', '#4f7be4', '#b9b9c0', '#edecf0']
                //'legend': {'position': 'bottom'}
              };
    
        }
        // Convert condArray into the DataTable that Google Charts needs and put it in a var
        var data = google.visualization.arrayToDataTable(condArray)
      
        // Display chart inside of the empty div element using the DataTable and Options set
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
      }
  }
  else{
    if(document.getElementById('clicktext') === null){
      var tt = document.getElementById('pointdetails');
      var ttg = document.getElementById('graphing');
      ttg.removeChild(tt);
      var elhold = document.getElementById('contentdynamic');
      var demo31 = document.getElementById('demo3');
      demo31.style.height = "7rem";
      elhold.style.fontSize = "13px";
      var divnode = document.createElement('div');
      divnode.id = "clicktext";
      divnode.style.padding = "0px";
      var bri = document.createElement("i");
      bri.className = "fas fa-map-marker-alt";
      const contentnode = document.createTextNode("Klicke mit der Maus auf einen Hotspot auf der Karte ( ");
      const contentnode2 = document.createTextNode(" ), um details angezeigt zu bekommen.");
      divnode.appendChild(contentnode);
      divnode.appendChild(bri);
      divnode.appendChild(contentnode2);
      elhold.appendChild(divnode);
    }
  }
  
  });




