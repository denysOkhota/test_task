from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["testapi_db"]

@app.route("/alert",methods=['POST',])
def index():
    print(request.json)
    return {"status":"success"}

@app.route('/api/<string:key>',methods=["GET",])
def get(key):

    key_value = db.values.find_one({"key":key})
    if key_value:
        return jsonify({'key': key, 'value': key_value['value']})
    else:
        return jsonify({'status': 'Value not found'}), 404

@app.route('/api', methods=['POST',])
def post():
    key = request.json['key']
    value = request.json['value']
    r=db.values.insert_one({'key': key, 'value': value})
    print(type(r),r)
    return jsonify({'key': key, 'value': value}), 200

@app.route('/api',methods=["PUT",])
def update():
    key = request.json['key']
    value = request.json["value"]
    db.values.update_one({'key':key},{'$set':{'key':key,'value':value}})
    return jsonify({'key': key, 'value': value}), 200