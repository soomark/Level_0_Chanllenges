# Function to check if number is either even or odd
def even_odd(number):
    if number % 2 == 0:
        print("‘‘ even ’’")
    else:
        print("‘‘ odd ’’")


number = input('Enter the number: ')  # Input of number
number = int(number)
even_odd(number)
