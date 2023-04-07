"""
database = dictionary
keys: ids for the patients
value: dictionary: {"id": <id>, "name": "<name>, "blood_type": <bt>}

{1: {id: 1' name': "Jefferson", "blood_type": "0+"},

"""

from flask import Flask, request, jsonify
app = Flask(__name__)

db = {}

def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient


@app.route("/new_patient", methods=["POST"])
def post_new_patient(): # flask handler function
    # Get Input Data
    # Call other functions to do the work
    # Return a response
    in_data = request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    # Validate input
    # Do the work
    # Return an answer
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400

    add_patient_to_db(in_data(["id"], in_data["name"], in_data["blood_type"]))

    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"

    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]

    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:  # does the key exist?
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type, has type {}".format(key, type(in_data[key]))

    return True


if __name__ == "__main__":
    app.run()