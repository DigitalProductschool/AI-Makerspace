Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ZTY4MDhiZS02NjI4LTQ1ZTctODhlMi01MmE2MmIyNDA1ZDUiLCJpZCI6MzYzNzcsImlhdCI6MTYwMzQyNTMzMH0.1jC4HVXKgDm4gxUshm8dZtDoM23dyl2zRpuM_z0Coig';
var viewer = new Cesium.Viewer('cesiumContainer', { 
timeline: false,
animation: false,
terrainProvider: Cesium.createWorldTerrain()
});
viewer._cesiumWidget._creditContainer.style.display = "none";

const buildingsTileset = viewer.scene.primitives.add(Cesium.createOsmBuildings());
// Fly the camera to Mount Everest at the given longitude, latitude, and height.
viewer.camera.flyTo({
  destination : Cesium.Cartesian3.fromDegrees(86.922623, 27.986065, 9000.0),
  orientation : {
      heading : Cesium.Math.toRadians(175.0),
      pitch : Cesium.Math.toRadians(0.0),
      roll : 0.0
  }
});


