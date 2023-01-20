def interface():
    print("Blood Calculator")
    while True:
        print("Select an option:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Select an option: ")
        
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()

    print("Program ended")

def HDL_driver():
    value = HDL_input()
    result = HDL_analysis(value)
    HDL_output(value,result)

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

def HDL_output(HDL_value,HDL_analysis):
    print("The HDL result of {} is considered {}".format(HDL_value,HDL_analysis))
    return

def LDL_input():
    LDL_value = int(input("Enter the LDL result: ")
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
    
interface()
