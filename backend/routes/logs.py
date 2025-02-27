from flask import Blueprint, jsonify
import json

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/get_logs', methods=['GET'])
def get_logs():
    with open("flight_logs.json", "r") as file:
        logs = json.load(file)
    return jsonify(logs)
