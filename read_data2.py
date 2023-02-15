## This is how you test a function that reads data ##
def read_file(filename):  # All this function does in input/output...no test
    in_file = open("input_data.txt", "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)

def analyze_ID(input_line):
    patient_data = input_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id
    
## Example testing function ##

def test_read_file():
    from module import read_file
    filename = "input_data2.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected