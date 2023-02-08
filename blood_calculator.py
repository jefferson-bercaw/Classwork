print("This is the blood_calculator.py file")
print("Python thinks this is called {}".format(__name__))


def interface():
    print("Blood Calculator")
    while True:
        print("Select an option:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Select an option: ")

        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Chol_driver()

    print("Program ended")


def HDL_driver():
    value = HDL_input()
    result = HDL_analysis(value)
    HDL_output(value, result)


def HDL_input():
    HDL_value = int(input("Enter the HDL result: "))
    return HDL_value


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline low"
    else:
        answer = "Low"

    return answer


def HDL_output(HDL_value, HDL_analysis):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analysis))
    return


def LDL_driver():
    value = LDL_input()
    answer = LDL_analysis(value)
    LDL_output(value, answer)


def LDL_input():
    LDL_value = int(input("Enter the LDL result: "))
    return LDL_value


def LDL_analysis(LDL_int):
    if LDL_int >= 190:
        answer = "Very high"
    elif LDL_int >= 160:
        answer = "High"
    elif LDL_int >= 130:
        answer = "Borderline high"
    else:
        answer = "Normal"
    return answer


def LDL_output(value, answer):
    print("The LDL result of {} is considered {}".format(value, answer))


def Chol_driver():
    value = Chol_input()
    answer = C_analysis(value)
    C_output(value, answer)


def Chol_input():
    C_value = int(input("Enter the Cholesterol result: "))
    return C_value


def C_analysis(val):
    if val >= 240:
        answer = "High"
    elif val >= 200:
        answer = "Borderline high"
    else:
        answer = "Normal"
    return answer


def C_output(val, ans):
    print("The cholesterol result of {} is considered {}".format(val, ans))


if __name__ == '__main__':
    interface()
