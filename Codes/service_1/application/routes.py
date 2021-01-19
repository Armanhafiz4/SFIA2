from application import app 
import requests

@app.route('/')
def index(): 
    strength_response = requests.get("http://player-backend:5000/strength")
    weakness_response = requests.get("http://player-backend:5000/weakness")
    position_response = requests.post("http://player-backend:5000/position", json={"strength" : strength_response.text, "weakness" : weakness_response.text})
    return render_template("index.html", strength=strength_response.text, weakness=weakness_response.text, position=position_response.get_json())
    




