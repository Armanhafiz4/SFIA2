from application import app
from flask import request, jsonify

@app.route("/position", methods=["POST"])
def get_position():
    suited_positions = {"pace" : "winger", "defending" : "centreback", "shooting" : "striker"}
    strength = request.get_json()["strength"]
    unsuited_positions = { "passing" : "striker", "dribbling" : "centreback", "heading" : "winger"}
    weakness = request.get_json()["weakness"]
    app.logger.info(strength)
    app.logger.info(weakness)
    return jsonify({ "suited_position" : suited_positions[strength], "unsuited_position" : unsuited_positions[weakness] })