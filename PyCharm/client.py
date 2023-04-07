import requests

server = "http://127.0.0.1:5000"

r = requests.get(server + "/info")

print(r.status_code)
print(r.text)

out_data = {'name': "Jefferson", "hdl_value": 65}
r = requests.post(server + "/HDL_analysis", json=out_data)
print(r.status_code)
print(r.text)

out_data = {"a": 2, "b": 3}
r = requests.post(server + '/add', json = out_data)
print(r.status_code)
print(r.json())

r = requests.get(server + '/add_two/5/26')
print(r.json())