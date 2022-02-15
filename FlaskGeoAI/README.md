# AI Maker Space | Rapid Prototyping 101 of Geo AI problem statements #DPS

Let's go digital with this quick workshop on rapid prototyping on geo ai problem statements. I will walk you through on making digital product with a 'Flask' backend from nothing to building powerful end to end web applications.
<p class="ex1" align="justify">  <br />
We will walk through 7 phases of this workshop:<br />
✣ <b>1 | Basic Flask server : </b> We will host a basic Flask server in Heroku and we will go digital. We will all have a digital presence and have a basic web-application running in a web address. <br />
✣ <b>2 | Design, UI and Responsive : </b> We will add cool designs and UI in our web-application keeping User eXperience (UX) in mind. We will now have a cooler presence online. <br />
✣ <b>3 | User Input & Databases : </b>  We will interact with users and take their input in with different forms. We will also learn how to store the data in databases such as Firebase, MongoDb etc. <br />
✣ <b>4 | Mapbox Map & Mongodb: </b> We will learn to add a map in our webapplication and fetch data to display in map from Mongodb database. We will learn on how to add responsive designs, markers, 3D objects, 3D buildings, live traffic, API data or geojson data over map. <br />
✣ <b>5 | 3D Maps, AR & 3D Interactive Applications : </b>  We will learn on how to build 3D maps, build amazing interactive 3D applications and also other Mixed reality applications with web frameworks.<br />
✣ <b>6 | Deep Learning: </b>  We will learn on how to access cutting edge Deep Learning models from our Flask server itself and display the results on user request over an input.<br />
✣ <b>7 | ML API @ VM & App Engine : </b>  We will learn on how to make Deep Learning API and serve it with Virtual Machine or Google App Engine via Docker. We will also learn to fetch data from our API to display results in our webapplication or store results in Mongodb.<br />
</p>

<p class="ex1" align="justify">  <br />
The web application/code is open sourced and feel free to take inspiration to build your own prototype. Some of the code in 2 | Design section is taken from *code pen* (open source) to highllight design possibilities. You will find a readme in each folder with proper instructions on how to get started building your own digital product.
</p>

# What's Missing?

I have removed the tokens, credentials required from the following sections but feel free to add your own credentials to make it work flawlessly. NOTE: Always pass credentials from  Flask server and do not store in your static pages.

```js
mapboxgl.accessToken in './v7-glcoud-docker/app/static/js/4map/mapindex.js'
2x mongodb collection access username & password in 'v7-glcoud-docker/app/views.py/views.py'
openweathermap API token (app id) in function WeatherSource() in './v7-glcoud-docker/app/static/js/4map/mapindex.js'
maptiler API token in './v7-glcoud-docker/app/static/js/4map/aboutmap.js'
firebase credentials in 'v7-glcoud-docker/app/views.py' and './v7-glcoud-docker/firebase_certificate.json'

```
<img src="./final.gif" width=100%> 

author: @[s-ai-kia](https://github.com/s-ai-kia/)


Apart from the functionalities mentioned for Geo AI in this repository, several other geo frameworks can be integrated such as Google Earth Engine Code Editor outputs maps with access to proper satellite data (SAR, NDVI maps) such as COPERNICUS Sentinel, Jaxa ALOS etc. Also '[geemap](https://github.com/giswqs/geemap)' backend in Python makes integration in Flask easier.
