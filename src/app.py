"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from flask import jsonify
from flask import request
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get():
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def handle_new():
    request_body = request.data
    decoded_object = json.loads(request_body)
    if all (k in decoded_object for k in ("first_name","age", "lucky_numbers")):
        jackson_family.add_member(decoded_object)
        return jsonify(), 200
    else:
        return jsonify("wrong info"), 400
    
@app.route('/member/<int:member_id>', methods=['GET'])
def handle_get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if (member != None):
        response_body = {
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
        }
        return jsonify(response_body), 200
    else:
        return jsonify("wrong info"), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def handle_delete(member_id):
    member = jackson_family.delete_member(member_id)
    if (member):
        response_body = {
        "done": "True"
        }
        return jsonify(response_body), 200
    else:
        return jsonify("wrong info"), 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
