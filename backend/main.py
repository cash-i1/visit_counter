from flask import Flask
import json

app = Flask(__name__)

def get_json():
    with open("./visits.json", "r") as file:
        return json.loads(file.read())
        
def write_json(json_data):
    with open("./visits.json", "w") as file:
        return json.dump(json_data, file)

@app.route('/add_1')
def add_1():
    json = get_json()
    json["visits"] += 1
    write_json(json)
    return json

if __name__ == "__main__":
    app.run()
    #sd