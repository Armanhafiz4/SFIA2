from application import app
from flask import request, Response 

@app.route("/position", methods=["POST"])
def get_position():
    positions = [ "pace" = "winger", "defending" = "centreback", "shooting" = "striker"]
    strength = request.data.decode("utf-8")
    positions = [ "passing" = "striker", "dribbling" = "centreback", "heading" = "winger"]
    weakness = request.data.decode("utf-8")
    return Response(positions[strength, weakness] , mimetype='text/plain')