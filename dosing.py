"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def display_diagnosis_screen():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")


def get_diagnosis():
    diagnosis = int(input("Enter a number: "))
    return diagnosis


def display_weight_screen():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")


def get_weight_in_kg():
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]

    if units == "lb":
        weight = weight / 2.205

    return weight


def calculate_dose(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def display_dose(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


def main_screen_driver():
    display_diagnosis_screen()
    diagnosis = get_diagnosis()
    display_weight_screen()
    weight = get_weight_in_kg()

    dosage_mg_first_day = calculate_dose(diagnosis, weight)
    display_dose(weight, dosage_mg_first_day)


if __name__ == '__main__':
    main_screen_driver()
