import requests

m = {"user": "jrb187", "message": "Let's go wolfpack"}

#r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message', json=m)
r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/jpk41")
print(r.json())