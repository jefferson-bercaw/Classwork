in_file = open("input_data.txt", 'r')  # r=read, w=write, n=append
fruits = in_file.readlines()  # reads data from file object variable
print(fruits)
in_file.close()  # closes file

# Or, for large files #

in_file = open("input_data.txt", 'r')

for line in in_file:  # iterates over each line in the file
    print(line)
    
## Read in a single line in file (can't go backwards) ##

first_fruit = in_file.readline()
second_fruit = in_file.readline()

