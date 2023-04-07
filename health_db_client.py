import requests

server = '' \

patient = {"id": 1, "name": "David", "blood_type": "O+"}

r = requests.post(server + "/new_patient", json=patient)

print(r.status_code)
print(r.json())