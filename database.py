def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    new_patient = {'First Name': first_name,
                    'Last Name': last_name,
                    'MRN': patient_mrn,
                    'Age': patient_age,
                    'Tests': []}
    return new_patient


def main_driver():
    db = []

    db.append(create_patient_entry("Ann", "Ables", 1, 34))
    db.append(create_patient_entry("Jeff", "Jeff", 2, 63))
    db.append(create_patient_entry("Bob", "Saget", 3, 11))


    add_test_to_patient(db, 3, "HDL", 120)
    add_test_to_patient(db, 3, "LDL", 68)


    
    # room_numbers = ["103", "232", "333"]
    # print_directory(db, room_numbers)

    res = find_result(db, 3, "HDL")
    print(res)
    
    print_database(db)
    print(db)
    return


def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))

        # OR

    # for patient,room_num in zip(db,room_numbers):
    #     print("Patient {} is in room {}".format(patient[0],room_num))


def find_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    if patient is False:
        print("MRN #{} not found".format(mrn))

    for test_info in patient["Tests"]:
        if test_info[0] == test_name:
            return test_info[1]

    return False


def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient['MRN'] == mrn_to_find:
            return patient
    return False


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)

    if patient is False:
        print("Bad entry")
    else:
        patient["Tests"].append([test_name, test_value])
    return


def get_full_name(patient_dict):
    full_name = patient_dict["First Name"] + ' ' + patient_dict["Last Name"]
    return full_name
    
def print_database(patient_dict):
    for patient in patient_dict:
        print("MRN: {}, Full Name: {}, Age: {}".format(patient["MRN"], get_full_name(patient), patient["Age"]))
        

if __name__ == '__main__':
    main_driver()
