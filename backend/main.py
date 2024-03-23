from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_json():
    with open("./backend/visits.json", "r") as file:
        return json.loads(file.read())
        
def write_json(json_data):
    with open("./backend/visits.json", "w") as file:
        return json.dump(json_data, file)

@app.route('/add_1')
def add_1():
    json = get_json()
    json["visits"] += 1
    write_json(json)

    response = jsonify(json)

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    return response

if __name__ == "__main__":
    app.run()
    #sd