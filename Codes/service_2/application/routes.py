from application import app 
from flask import request, Response 
import random

@app.route("/strength", methods=["GET"])
def get_strength():
    strengths = [ "pace", "defending", "shooting"]
    return Response(str(random.choice(strengths)), mimetype='text/plain') 