# Function to convert Celsius to Fahrenheit
def celc(c):
    fahrenheit = 9/5 * c + 32  # Formula to convert Celsius to Fahrenheit
    return fahrenheit


# Function to convert  Fahrenheit to Celsius
def fahr(f):
    celsius = (f - 32) * 5/9  # Formula to convert Celsius to Fahrenheit
    return celsius


#Input of values
x = float(input("Enter Celsius number: "))
y = float(input("Enter Fahrenheit number: "))

# call function convert Celsius to Fahrenheit
x1 = celc(x)

# call function convert Fahrenheit to Celsius
y1 = fahr(y)

# Celsius to Fahrenheit Output
print(str(x) + " degree Celsius is equal to " + str(x1) + " degree Fahrenheit")

# Fahrenheit to Celsius Output
print(str(y) + " degree Fahrenheit is equal to " + str(y1) + " degree Celsius")
