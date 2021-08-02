from flask import Flask , jsonify, request
from data import data
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/')
def data_planets():
    return jsonify({
        "data" : data,
        "message" : "suceess"
    },200)

@app.route('/data_planet')
def planetData():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name )
    return jsonify({
        "data" : planet_data,
        "message" : "success"
    },200)


# if __name__ == "__main__":
#     app.run()