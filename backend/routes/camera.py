from flask import Blueprint, Response
import cv2

camera_bp = Blueprint('camera', __name__)

def generate_frames():
    cap = cv2.VideoCapture(0)  # Change URL for drone feed
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@camera_bp.route('/live_feed')
def live_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
