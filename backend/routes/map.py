from flask import Blueprint, request, jsonify

map_bp = Blueprint('map', __name__)

@map_bp.route('/navigate', methods=['POST'])
def navigate():
    data = request.json
    lat, lon = data["latitude"], data["longitude"]
    # Send coordinates to drone
    return jsonify({"message": f"Navigating to {lat}, {lon}"}), 200
