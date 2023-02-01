def create_patient_entry(patient_name,patient_mrn,patient_age):
    new_patient = [patient_name,patient_mrn,patient_age]
    return new_patient
    
def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables",1,34))
    db.append(create_patient_entry("Jeff Jeff",2,63))
    db.append(create_patient_entry("Bob Saget",3,11))
    print(db)
    
    
if __name__ == '__main__':
    main_driver()