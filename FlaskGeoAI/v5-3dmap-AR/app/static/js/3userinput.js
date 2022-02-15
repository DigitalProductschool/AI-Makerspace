/*mongodb form */

(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();


  /* 360 photo */
  // Create viewer
  viewer = pannellum.viewer('panorama', {
    "type": "equirectangular",
            "autoLoad": true,
    "panorama": "https://pannellum.org/images/bma-1.jpg",
            "hotSpots": [
                {
                    "pitch": 14.1,
                    "yaw": 1.5,
                    "cssClass": "custom-hotspot",
                    "createTooltipFunc": hotspot,
                    "createTooltipArgs": "Baltimore Museum of Art"
                }, 
                {
                    "pitch": -9.4,
                    "yaw": 222.6,
                    "cssClass": "custom-hotspot",
                    "createTooltipFunc": hotspot,
                    "createTooltipArgs": "Art Museum Drive"
                },
                {
                    "pitch": -0.9,
                    "yaw": 144.4,
                    "cssClass": "custom-hotspot",
                    "createTooltipFunc": hotspot,
                    "createTooltipArgs": "North Charles Street"
                }
            ]
  });
        
// Hot spot creation function
function hotspot(hotSpotDiv, args) {
    console.log(hotSpotDiv);
    console.log(args);
    hotSpotDiv.classList.add('custom-tooltip');
    var span = document.createElement('span');
    span.innerHTML = args;
    hotSpotDiv.appendChild(span);
    span.style.width = span.scrollWidth - 20 + 'px';
    span.style.marginLeft = -(span.scrollWidth - hotSpotDiv.offsetWidth) / 2 + 'px';
    span.style.marginTop = -span.scrollHeight - 12 + 'px';
}


/*
* Hello and welcome to image viewer
*
* Expand images by clicking them.
*/

// Here is our function that makes the magic happen.
// When new images are added call this function again
// to assign the event listeners.
function imageViewer () {
    // Lets start by collecting all of the images
    // with our special class and also grabing the output container
    let imgs = document.getElementsByClassName("img"),
        out  = document.getElementById("img-out");
  
    // Next lets assign an event listener to each image
    // by looping through them
    for(let i = 0; i < imgs.length; i++) {
  
      // We need to make sure we dont add listeners more than one time 
      // to an image
      if(!imgs[i].classList.contains("el")){
        
        imgs[i].classList.add("el");
      // In this listener we are going to toggle a special class
      // that will highlight the image container
        imgs[i].addEventListener("click", lightImage);
        function lightImage(){
          let container = document.getElementsByClassName("img-panel")[i];
          container.classList.toggle("img-panel__selct");
        };
  
        // Now we are going to create a second listener and let
        // It render the image to the user.
        imgs[i].addEventListener("click", openImage);
        function openImage () {
          let imgElement = document.createElement("img"),
              imgWrapper = document.createElement("div"),
              imgClose   = document.createElement("div"),
              container  = document.getElementsByClassName("img-panel")[i];
          container.classList.add("img-panel__selct");
          imgElement.setAttribute("class", "image__selected");
          imgElement.src = imgs[i].src;
          imgWrapper.setAttribute("class", "img-wrapper");
          imgClose.setAttribute("class", "img-close");
          imgWrapper.appendChild(imgElement);
          imgWrapper.appendChild(imgClose);
  
  
          setTimeout(
            function(){ 
              imgWrapper.classList.add("img-wrapper__initial");
              imgElement.classList.add("img-selected-initial");
            }, 50);
  
          out.appendChild(imgWrapper);
          imgClose.addEventListener("click", function(){
            container.classList.remove("img-panel__selct");
            out.removeChild(imgWrapper);
          });
        }
      }
    }
  }
  imageViewer();
  
  
  
  //==================================================
  // This is code I modified from a github repo by me
  // Repo:
  //
  //    https://github.com/matthewLeFevre/picRender
  //
  // It is not required for the image viewer but 
  // I am adding it for interactivity 
  //--------------------------------------------------
  
  let picRender = {
    imgObjArr: [],
    imgInput : document.getElementById("img-upload"),
    imgOutput: document.getElementById("display-box"),
    
    //==================================================
    // standalone Helper Functions
    //==================================================
    // Generate a random 5 character string of numbers
    generateRandomId: function () {
      let id = "";
      // Addjust the length of the id by changing for loop
      for (let i = 0; i < 5; i++) {
        id += Math.floor((Math.random() * 10) + 1);
      }
      return id;
    },
    
    //==================================================
    // Render Uploaded Images
    //==================================================
    renderImages: function () {
      picRender.imgInput.addEventListener("change", function(){
        for (let i = 0; i < picRender.imgInput.files.length; i++) {
          let randomId = picRender.generateRandomId(),
              imgObj   = {
                imgEl   : document.createElement("img"),
                imgPanel: document.createElement("div"),
                fileData: picRender.imgInput.files[i],
                fileName: picRender.imgInput.files[i].name,
                fileSize: picRender.imgInput.files[i].size,
                fileId  : "fileId_" + picRender.imgInput.files[i].name + randomId,
                
                configImage: function () {
                  this.imgEl.setAttribute("class", "img");
                  this.imgEl.src = URL.createObjectURL(this.fileData);
                  this.imgPanel.setAttribute("id", this.fileId);
                  this.imgPanel.setAttribute("class", "img-panel");
                  this.imgPanel.appendChild(this.imgEl);
                  picRender.imgOutput.appendChild(this.imgPanel);
                  imageViewer();
                }
              };
          imgObj.configImage();
          picRender.imgObjArr.push(imgObj);
        };
      });
    },
  
  }
  
  picRender.renderImages();
  
  /*
  ** Working on making this thing a class
  */
  
  class ImageViewer {
    constructor(imgArr, imgContArr, imgOutput) {
      this.imgArr     = imgArr;
      this.imgContArr = imgContArr;
      this.imgOutput   = imgOutput;
      this.initialize();
    }
    
    initialize () {
      for( let i = 0; i < this.imgArr.length; i++) {
        
        let img = this.imgArr[i];
        
        if(!img.classList.contains("el")) {
       
          img.classList.add("el");
          img.addEventListener("click", function (){         
            
            let imgElement = document.createElement("div"),
                imgWrapper = document.createElement("div"),
                imgClose   = document.createElement("div"),
                container = this.imgContArr[i];
            
            container.classList.toggle("img-panel__selct");
            imgClose.setAttribute("class", "img-close");
            imgElement.setAttribute("class", "image__selected");
            imgElement.src = imgs[i].src;
            imgWrapper.setAttribute("class","img-wrapper");
            imgWrapper.appendChild(imgElement);
            imgWrapper.appendChild(imgClose);
            
            setTimeout(
            function (){
              imgWrapper.classList.add("img-wrapper__initial");
              imgElement.classList.add("img-selected-initial");
            }, 50);
            
            this.imgOutput.appendChild(imgWrapper);
            
            imgclose.addeventListener("click", function(){
              container.classList.remove("img-panel__selct");
              this.imgOutput.removeChild(imgWrapper);
            })
                
          });
        
        }
        
      }
      
    }
    
  }