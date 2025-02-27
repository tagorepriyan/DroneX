from flask import Blueprint, request, jsonify

drone_bp = Blueprint('drone', __name__)

@drone_bp.route('/start', methods=['POST'])
def start_drone():
    # Command to start the drone
    return jsonify({"message": "Drone started"}), 200

@drone_bp.route('/stop', methods=['POST'])
def stop_drone():
    # Command to stop the drone
    return jsonify({"message": "Drone stopped"}), 200
