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
    print(result)

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


interface()
