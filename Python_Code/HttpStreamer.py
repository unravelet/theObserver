from flask import Flask, Response
import cv2

# https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00
# initialize a flask object

class EndpointAction(object):
    def __init__(self, action, status = 200, headers = {}):
        self.action = action
        self.status = status
        self.headers = headers

    def __call__(self, *args):
        return self.action()

class HttpStreamer(object):
    def __init__(self, action):
        self.flask_app = Flask(__name__)
        self.action = action

    def run(self):
        self.add_all_endpoints()
        self.flask_app.run()

    def add_all_endpoints(self):
        self.add_endpoint(endpoint="/", endpoint_name="/", handler=self.index)
        self.add_endpoint(endpoint="/video_feed", endpoint_name="/video_feed", handler=self.video_feed)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.flask_app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler)) 

    #########

    def index(self):
        return Response('Hello watchers! 🕶', status=200, headers={})
    
    def video_feed(self):
        return Response(self.action(), mimetype="multipart/x-mixed-replace; boundary=frame")
