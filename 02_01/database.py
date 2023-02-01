def create_patient_entry(patient_name,patient_mrn,patient_age):
    new_patient = [patient_name,patient_mrn,patient_age]
    return new_patient
    
def main_driver():
    db = []
    
    db.append(create_patient_entry("Ann Ables",1,34))
    db.append(create_patient_entry("Jeff Jeff",2,63))
    db.append(create_patient_entry("Bob Saget",3,11))
    
    print(db)
    print("Get Patient Ann")
    found_patient = get_patient_entry(db,4)
    
    if found_patient is False:
        print("Patient mrn {} not found".format(found_patient))
    else:
        print(found_patient)
        
def get_patient_entry(db,mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False
    


if __name__ == '__main__':
    main_driver()