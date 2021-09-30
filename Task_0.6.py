#Function hat takes in three numbers and returns the maximum number
def maximum(num1, num2, num3):
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
        print("Largest number is: ", largest)


num1 = input('Enter your 1st value: ')
num1 = int(num1)
num2 = input('Enter your 2nd value: ')
num2 = int(num2)
num3 = input('Enter your 3rd value: ')
num3 = int(num3)
maximum(num1, num2, num3)