from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_visits():
    with open("./backend/visits.txt", "r") as file:
        return file.read()
        
def write_visits(data):
    with open("./backend/visits.txt", "w") as file:
        return file.write(str(data))

@app.route('/add_1')
def add_1():

    visits = get_visits() 
    print(visits)
    new_value = int(visits) + 1
    print(new_value)
    write_visits(new_value)

    response = jsonify(new_value)

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    return response

if __name__ == "__main__":
    app.run()
    #sd