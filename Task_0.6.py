#Function hat takes in any three numbers and returns the maximum number
def maximum(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    return largest


# call function
value = maximum(-3, -2, -5)

print(f'Largest value is {value}')
