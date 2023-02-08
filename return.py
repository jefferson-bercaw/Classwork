def increment_by_five(x):
    answer = x + 5
    print("The answer is {}".format(answer))


#    if answer == 15:
#        print("Bad input")
#        return # leave function
    return answer, True


y = increment_by_five(10)  # creates tuple
print(y[0])
print(y[1])
