function addLayer7() {
  const address2 = fetch("/data2").then((response) => response.json()).then((user) => {
      return user;
  });
  
  const printAddress2 = async () => {
  const a2 = await address2;
  var awhite = new Array();
  var ablue = new Array();
  var ared = new Array();

  for(let i=0; i<a2.length;i++){
    if(a2[i].properties.intensity === 0){
      awhite.push(a2[i]);
    }
    else if(a2[i].properties.intensity === 1){
      ablue.push(a2[i]);
    }
    else{
      ared.push(a2[i]);
    }
  }

  var n1 = 27;
  var n2 = 19;
  let randomwhite = awhite.sort(() => .5 - Math.random()).slice(0,n1)
  let randomblue = ablue.sort(() => .5 - Math.random()).slice(0,n2)


  // const datalinks = [awhite, ablue, ared]
  const datalinks = [randomwhite, randomblue, ared]
  // experimental 
  const images = [{url:'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAuCAYAAAA/SqkPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF+mlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTEwLTAzVDE0OjE5OjE4KzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMC0wM1QxNDoyNDoxMiswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMS0xMC0wM1QxNDoyNDoxMiswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpjNmY1ZGExNS0xOTYwLTQ4NGEtOThjZS01NmJhNzAxNDg3MDkiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo4MDc0OTgwOS1hYzZiLTYzNDEtYjcyNS1lYjU5N2M0MGRkZWUiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDozM2MxMGNkOC1lMTE0LWNkNGItOGY1Yy05ZjgyNzY0MTE0MTAiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjMzYzEwY2Q4LWUxMTQtY2Q0Yi04ZjVjLTlmODI3NjQxMTQxMCIgc3RFdnQ6d2hlbj0iMjAyMS0xMC0wM1QxNDoxOToxOCswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpjNmY1ZGExNS0xOTYwLTQ4NGEtOThjZS01NmJhNzAxNDg3MDkiIHN0RXZ0OndoZW49IjIwMjEtMTAtMDNUMTQ6MjQ6MTIrMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6nN8t1AAAA8ElEQVRYhe2XUQ7EIAhE0fT+9/JU3Y+NjesiBRQkaee3wnNoncZUSgGmTua6xFl0LAT268kN5MXQvnZYPwKTRYoNsMCrgGTPHmwBRXvn0QNr+N3HZaYK9nBbdbZgd2XwdXuJk1yY+lQSp5tm1FgUsvK5lRRMAUTw7cfpBYcDU8dGdKQ0jrF/tTiEDvgeA016zSRe2v6OxckzodSC3dWCPV27O77MhRg1gO24f3qHcQxg4/qvZyjHAGtdo70oxyvgwx7hRl0143rqYm4mDljj+rYmtGMAmWvWWoljTkP2BsOPuuqZd6ct11QMpEq3baP+AP94HcXsBKMxAAAAAElFTkSuQmCC', id:'custom-marker2white'},{url:'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAuCAYAAAA/SqkPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF+mlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTEwLTAzVDE0OjE5OjE4KzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMC0wM1QxNDoyMzoyNSswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMS0xMC0wM1QxNDoyMzoyNSswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDplZTIwYzQ3My1jZTE0LTRlNDctYjk3OC1lYzI4MDBkYzZjYjUiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDozMjcxYzVlYy00N2E3LTAzNGEtYTI4YS01YmU1MTdkMGM1MGIiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDphZjIxZTA1Yi04MmU2LWE3NDQtODk2My0yZjEwZWQ5M2U4ZGEiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmFmMjFlMDViLTgyZTYtYTc0NC04OTYzLTJmMTBlZDkzZThkYSIgc3RFdnQ6d2hlbj0iMjAyMS0xMC0wM1QxNDoxOToxOCswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDplZTIwYzQ3My1jZTE0LTRlNDctYjk3OC1lYzI4MDBkYzZjYjUiIHN0RXZ0OndoZW49IjIwMjEtMTAtMDNUMTQ6MjM6MjUrMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6BlekIAAAC9UlEQVRYhb3YTagVdRjH8c+ZjhbaCxmBBKJI2AtJr9xWQauoQDfWImoTBkZktShoV0G1CSoQTdy0iEIwJHEhKLoQJXqxa9GiTOIWUUhmi2tFmfe6eO7g8Thz5plzz/EHB87MPP/n+//PPPM8z386HpyV1J24H3dgGbooB/+CoziETzPOugmbpViHx3AbrqmxW4Pj+BAf4bdBTjsNK34JL2NJYoK9+hOb8Cb+bQO+FVtxX0tgv77EU/i6/0JRYXw3vhgBFO7BETzUBF6B/Vg0Amipy/AxVteBu9iuPnjmo0XYgcVV4I24dwzQUjeJYMX54LoSP+L6MYJhGitxslzxI5cAClfhCeK5rsSjLR18IiL/DCbExLNah3e7Ig1mn+33WI/Dfedvx7a5STRpAssLkQavSwyYxsMVUCJBrMWJhJ+FuKvAjQlj2CwCsE4n8HrS1wOFfB7embDZhb8TdrcUIkAy+ithM50Eny3EPc8o87otwbUJu4UFTiXB6xM2G0RubtJkgc9xNmH8uHgH6zSB5xJ+4IMCe0TdbFIhqswLuKLv2pM4UHG+SsdxpDsH3S6fRN7Bs5gSPddSkQuy2omZskiswDEsaOFgGM2KRmOyLBJT4paPW4cxyYX1ePMlAG8r//SC94qKMy79JILzIjBsGSN4C/4pD/rb20I872Ujhv4hAvh0L6hXM3h1xFB4qxdKdUPfxQ9ihqPQ76LLuQBc1dD/L19XM3q7H0r9FqbAZ2InMB/9LLLadBWgSjN4bZ5QeKMKSvNu8aDh91DHRBNfqboVl3re+c13W20cdLEJPCkqV1vtE5mwVk23Gm4Qr1ebHeRqfDvIoGnF8CteaQHd1AQlt2K4HN9pTiqnsEqkyIHKrJj4jpHpp17MQAPcIfnbrWPXAF9f4f0MtC2YaPT+q/H1TBYa4BnSv1lTqvP4eyLFppUNrl4twDe4ee74pKg+lamxTtng6tUZHRt6jp9uC2W4FZc6KHrqVcMMznzLrNNWXD3s4HPQmqCgwTZ6QQAAAABJRU5ErkJggg==', id:'custom-marker2blue'},{url:'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAuCAYAAAA/SqkPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF+mlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTEwLTAzVDE0OjE5OjE4KzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMC0wM1QxNDoyMzo1MCswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMS0xMC0wM1QxNDoyMzo1MCswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoyYTQ3MmFjYi0xYTRkLTFlNDktYjkwMC0yYTgwMDFhNzljODQiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDoxOWI5YjM4MC1jMzJmLTlmNDYtYWIzNS0xMzA2OWM1MDRkODEiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDowYjQxZDAyMC1kMzBjLWEyNDctYjgwOC03MTU2NjFlNjdjMjEiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjBiNDFkMDIwLWQzMGMtYTI0Ny1iODA4LTcxNTY2MWU2N2MyMSIgc3RFdnQ6d2hlbj0iMjAyMS0xMC0wM1QxNDoxOToxOCswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDoyYTQ3MmFjYi0xYTRkLTFlNDktYjkwMC0yYTgwMDFhNzljODQiIHN0RXZ0OndoZW49IjIwMjEtMTAtMDNUMTQ6MjM6NTArMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7UC3JVAAAA8klEQVRYhe2XQQ7EIAhF0XTZ+x9wLtIuGhvrIAUUJJn52wrPT+tvTJ99B6YO5rrEWbRNBLbryQ3kydC2tlvfA5NFig2wwLOAZM8WbAFFe+feA2v428dlpgL2cFt01GB3ZfB1e4uTXJjaVBKnm2bUWBSy8rmWFEwBRPDlx+kPDgemjo3oSGkcY/9qcQhtcB0DTXqNJF5a/o7FyTOgVIPdVYM9Xbs7vs2FGDWA7bgfvcM4BrBx/dUzlGOAua7RXpTjGfBuj3CjLhpxPXQxNxMHrHH9WhPaMYDMNWutxDGnIXuD4Udd9Jt3pyXXVAykSrdloz4BBl8cZIYdK5gAAAAASUVORK5CYII=', id:'custom-marker2red'}]

  Promise.all(
    images.map(img => new Promise((resolve, reject) => {
        map.loadImage(img.url, function (error, res) {
            if (error) throw error;
            map.addImage(img.id, res)
            resolve();
        })
    }))
    ).then(console.log("Marker Images Loaded"))
    

    // Add white points
    map.addSource('points2', {
      'type': 'geojson',
      'data': {
      'type': 'FeatureCollection',
      'features': datalinks[0]
      }
      });
        
    // Add a white symbol layer
    map.addLayer({
      'id': 'points2',
      "interactive": true,
      'type': 'symbol',
      'source': 'points2',
      'layout': {
      'icon-image': 'custom-marker2white',
      'visibility': 'none',
      // get the title name from the source's "title" property
      'text-field': ['get', 'title'],
      'text-font': [
      'Open Sans Semibold',
      'Arial Unicode MS Bold'
      ],
      'text-offset': [0, 1.25],
      'text-anchor': 'top'
      }
    });

    // Add blue points
    map.addSource('points3', {
      'type': 'geojson',
      'data': {
      'type': 'FeatureCollection',
      'features': datalinks[1]
      }
    });
          
    // Add a blue symbol layer
    map.addLayer({
      'id': 'points3',
      "interactive": true,
      'type': 'symbol',
      'source': 'points3',
      'layout': {
      'icon-image': 'custom-marker2blue',
      'visibility': 'none',
      // get the title name from the source's "title" property
      'text-field': ['get', 'title'],
      'text-font': [
      'Open Sans Semibold',
      'Arial Unicode MS Bold'
      ],
      'text-offset': [0, 1.25],
      'text-anchor': 'top'
      }
    });

    // Add red points
    map.addSource('points4', {
      'type': 'geojson',
      'data': {
      'type': 'FeatureCollection',
      'features': datalinks[2]
      }
    });
            
    // Add a red symbol layer
    map.addLayer({
      'id': 'points4',
      "interactive": true,
      'type': 'symbol',
      'source': 'points4',
      'layout': {
      'icon-image': 'custom-marker2red',
      'visibility': 'none',
      // get the title name from the source's "title" property
      'text-field': ['get', 'title'],
      'text-font': [
      'Open Sans Semibold',
      'Arial Unicode MS Bold'
      ],
      'text-offset': [0, 1.25],
      'text-anchor': 'top'
      }
    });
  }
  printAddress2();
}

map.on('style.load', () => {
  addLayer7();
  console.log('Marker points loaded!');
});

const targetDiv4 = document.getElementById("demo3");
const btn3 = document.getElementById("loaddata");
btn3.onclick = function () {

if(document.getElementById("dateselected1").value==="" && document.getElementById("dateselected2").value==="") { 
  alert("Please select 'Date (Datum)' from Suchfilter.");
} 
else if(document.querySelector('input[name="timeselect"]:checked').value==="3" && document.getElementById("timeselected1").value==="" && document.getElementById("timeselected2").value==="") { 
  alert("Please select 'Time (Uhrzeit): Individuell' from Suchfilter.");
}

else { 
    var btntext = document.getElementById("loaddata");
    if(btntext.innerHTML == 'SUCHEN')
    {


      btntext.innerHTML = 'KLAR';

      if (targetDiv4.style.display !== "block") {
        targetDiv4.style.display = "block";
      } else {
        targetDiv4.style.display = "none";
      }
      var visibility2 = map.getLayoutProperty(
              'points2',
              'visibility'
              );
      var visibility3 = map.getLayoutProperty(
              'points3',
              'visibility'
              );
      var visibility4 = map.getLayoutProperty(
              'points4',
              'visibility'
              );
      
      if (visibility2 !== "visible" && visibility3 !== "visible" && visibility4 !== "visible") {
        map.setLayoutProperty('points2', 'visibility', 'visible');
        map.setLayoutProperty('points3', 'visibility', 'visible');
        map.setLayoutProperty('points4', 'visibility', 'visible');
      } else {
        map.setLayoutProperty('points2', 'visibility', 'none');
        map.setLayoutProperty('points3', 'visibility', 'none');
        map.setLayoutProperty('points4', 'visibility', 'none');
      }
    
    
      let date1 = document.getElementById("dateselected1").value;
      let date2 = document.getElementById("dateselected2").value;
      let timeoption = document.querySelector('input[name="timeselect"]:checked').value;
    
      if(document.getElementById('zeitraumcontent') !== null){
        var el4 = document.getElementById('zeitraumcontent');
        el4.parentNode.removeChild(el4);
      }
  
      
      if(timeoption === "1"){
        document.getElementById("zeitraumcontentsmall").innerHTML = "<font size='1.5'>" + "Date : "+ date1 + " : " + date2 + "<br />"+ "Time : " + "6:00 - 9:00 Uhr" + "</font>";
      }
      else if(timeoption === "2"){
        document.getElementById("zeitraumcontentsmall").innerHTML = "<font size='1.5'>"+ "Date : " + date1 + " : " + date2 + "<br />"+ "Time : " + "16:00 - 19:00 Uhr" + "</font>";
      }
      else{
        
      let time1 = document.getElementById("timeselected1").value;
      let time2 = document.getElementById("timeselected2").value;
      document.getElementById("zeitraumcontentsmall").innerHTML = "<font size='1.5'>"+ "Date : " + date1 + " : " + date2 + "<br />"+ "Time : " + time1 + " - " + time2 + "</font>";
      }

  
    }
    else {
          /// Zeitraum dilemma
          if (targetDiv4.style.display !== "block") {
            targetDiv4.style.display = "block";
          } else {
            targetDiv4.style.display = "none";
          }
          var visibility2 = map.getLayoutProperty(
                  'points2',
                  'visibility'
                  );
          var visibility3 = map.getLayoutProperty(
                  'points3',
                  'visibility'
                  );
          var visibility4 = map.getLayoutProperty(
                  'points4',
                  'visibility'
                  );
          
          if (visibility2 !== "visible" && visibility3 !== "visible" && visibility4 !== "visible") {
            map.setLayoutProperty('points2', 'visibility', 'visible');
            map.setLayoutProperty('points3', 'visibility', 'visible');
            map.setLayoutProperty('points4', 'visibility', 'visible');
          } else {
            map.setLayoutProperty('points2', 'visibility', 'none');
            map.setLayoutProperty('points3', 'visibility', 'none');
            map.setLayoutProperty('points4', 'visibility', 'none');
          }

        
      if(document.getElementById('zeitraumcontentsmall') !== null){
      let el9u = document.getElementById('zeitraumcontentsmall');
      el9u.removeChild(el9u.childNodes[0]);
      el9u.innerHTML = "Wähler einen Zeitraum im Suchfilter";
      }

      btntext.innerHTML = 'SUCHEN';
      if(map.getLayer('points2') && map.getLayer('points3') && map.getLayer('points4')){
        map.removeLayer('points2');
        map.removeSource('points2');
        map.removeLayer('points3');
        map.removeSource('points3');
        map.removeLayer('points4');
        map.removeSource('points4');
        map.removeImage('custom-marker2white');
        map.removeImage('custom-marker2blue');
        map.removeImage('custom-marker2red');
        addLayer7();
      }
    }

  }
}

