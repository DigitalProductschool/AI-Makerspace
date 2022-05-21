from flask import Flask, request, send_file
from flask_cors import CORS
import numpy as np
import cv2
import io
import os
from inference import BGRemoval

app = Flask(__name__)
CORS(app)

model = None


@app.before_first_request
def load_model():
    global model
    model = BGRemoval()


@app.route('/', methods=["POST"])
def hello_background():
    global model
    image = request.data
    headers = request.headers
    red, green, blue, alpha = int(headers.get("red")), int(headers.get("green")), \
                              int(headers.get("blue")), int(headers.get("alpha"))
    # convert string of image data to uint8
    np_arr = np.frombuffer(image, np.uint8)
    # decode image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    model.load_image(img)
    model.run_model()
    out = model.remove_background(red, green, blue, alpha)
    out_img = cv2.imencode(".png", out)[1].tobytes()
    return send_file(io.BytesIO(out_img), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
