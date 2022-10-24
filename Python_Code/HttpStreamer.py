from flask import Response
from flask import Flask

import cv2

import Recognizer

# https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00
# initialize a flask object

app = Flask(__name__)

camera = cv2.VideoCapture(0)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(gen_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = Recognizer.getImage(Recognizer.hogDetector(frame), frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

if __name__ == "__main__":
    app.run(debug=True)