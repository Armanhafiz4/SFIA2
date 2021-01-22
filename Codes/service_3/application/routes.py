from application import app 
from flask import request, Response 
import random

@app.route("/weakness", methods=["GET"])
def get_weakness():
    weaknesses = [ "passing", "dribbling", "heading"]
    return Response(str(random.choice(weaknesses)), mimetype='text/plain')
