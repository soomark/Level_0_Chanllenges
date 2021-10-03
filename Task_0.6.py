#Function hat takes in three numbers and returns the maximum number
def maximum(num1, num2, num3):
    largest = 0
    if num1 > num2:
        if num1 > num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 > num3:
            largest = num2

        else:
            largest = num3

        # Display the largest number
        return largest


# call function
value = maximum(1, 2, 3)

# Output
print("Largest value is " + str(value))
