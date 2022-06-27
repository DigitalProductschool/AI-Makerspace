// add queryselectors for button
document.querySelector('#temp22').addEventListener('click', () => {
    document.querySelector('#temptemp').click();
});
document.querySelector('#traffi').addEventListener('click', () => {
    document.querySelector('#traffic').click();
});
document.querySelector('#smala2').addEventListener('click', () => {
    document.querySelector('#smala').click();
});
document.querySelector('#roads2').addEventListener('click', () => {
    document.querySelector('#road').click();
});
document.querySelector('#points_signal').addEventListener('click', () => {
    document.querySelector('#signal').click();
});
document.querySelector('#osm3d').addEventListener('click', () => {
    const styleJson2 = map.getStyle();
    if(styleJson2["name"] !== 'Mapbox Satellite'){
        document.querySelector('#b3D').click();
    }
    else{
        alert("3D buildings are not included in 'satellite' map style. Change map style to experience 3D buildings.");
    }
    
});