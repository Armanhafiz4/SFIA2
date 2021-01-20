from application import app 
from flask import render_template 
import requests

@app.route('/')
def index(): 
    strength_response = requests.get("http://football_gen_service_2:5000/strength")
    weakness_response = requests.get("http://football_gen_service_3:5000/weakness")
    position_response = requests.post("http://football_gen_service_4:5000/position", json={"strength" : strength_response.text, "weakness" : weakness_response.text})
    app.logger.info(position_response.json())
    return render_template("index.html", strength=strength_response.text, weakness=weakness_response.text, position=position_response.json())
    




