import requests

url = 'http://vcm-7631.vm.duke.edu:5002'

def get_patients():
    r = requests.get(url+'/get_patients/jrb187')
    d = r.json()
    return d

def get_blood_type(id):
    r = requests.get(url+'/get_blood_type/'+id)
    type = r.text
    return type

def post_match(out_data):
    r = requests.post(url + '/match_check', json=out_data)
    print(r.text)

if __name__ == '__main__':
    r = get_patients()
    print(r)
    id1 = r["Donor"]
    id2 = r["Recipient"]

    print(id1, id2)

    t1 = get_blood_type(id1)
    t2 = get_blood_type(id2)

    print(t1, t2)

    answer = "No"
    out_data = {"Name": "jrb187",
                "Match": "No"}
    post_match(out_data)

