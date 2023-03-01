import requests

out_data = {"name": "Jefferson Bercaw",
            "net_id": "jrb187",
            "e-mail": "jefferson.bercaw@duke.edu"}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)

