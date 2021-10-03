# Function to check if number is either even or odd
def even_odd(number):
    if number % 2 == 0:
        print('"even"')
    else:
        print('"odd"')


even_odd(int(input("Enter number: ")))
