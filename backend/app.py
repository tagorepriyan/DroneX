from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Initialize camera (Use 0 for webcam, or change to drone's camera feed URL)
camera = cv2.VideoCapture(0)

# Live Camera Feed
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode(".jpg", frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route("/live_feed")
def live_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Object Detection (Dummy Response)
@app.route("/detect")
def detect_objects():
    return jsonify({"status": "success", "detected_objects": ["Helmet", "QR Code", "Person"]})

# Start Drone
@app.route("/start", methods=["POST"])
def start_drone():
    return jsonify({"message": "Drone started"})

# Stop Drone
@app.route("/stop", methods=["POST"])
def stop_drone():
    return jsonify({"message": "Drone stopped"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
