from application import app, db  
from flask import render_template 
from sqlalchemy import desc 
import requests

class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    strength_type = db.Column(db.String(20), nullable=False)
    weakness_type = db.Column(db.String(20), nullable=False)
    position_type = db.Column(db.String(20), nullable=False)

@app.route('/')
def index(): 
    strength_response = requests.get("http://football_gen_service_2:5000/strength")
    weakness_response = requests.get("http://football_gen_service_3:5000/weakness")
    position_response = requests.post("http://football_gen_service_4:5000/position", json={"strength" : strength_response.text, "weakness" : weakness_response.text})
    app.logger.info(position_response.json())

    new_position = Positions(strength_type = strength_response.text, weakness_type = weakness_response.text, position_type = position_response.json()["suited_position"])
    db.session.add(new_position)
    db.session.commit()

    all_positions = Positions.query.order_by(desc("id")).limit(5).all()

    return render_template("index.html", strength=strength_response.text, weakness=weakness_response.text, position=position_response.json(), all_positions=all_positions)





