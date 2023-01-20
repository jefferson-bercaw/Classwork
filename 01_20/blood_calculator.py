def interface():
    print("Blood Calculator")
    while True:
        print("Select an option:")
        print("9 - Quit")
        choice = input("Select an option: ")
        
        if choice == "9":
            return

    print("Program ended")

def HDL_input():
    HDL_value = int(input("Enter the HDL result: "))
    return HDL_value


interface()
