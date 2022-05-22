# BGRemoval

A pre-trained portrait removal model [MODNET](https://github.com/ZHKKKe/MODNet).
The pretrained model is served in an API and is ready for deployment on CloudRun


## Requests
POST Request with binary body containing the image and the RGBA values to be replaced in the background in the headers

