# Function to convert Celsius to Fahrenheit
def celc(c):
    fahrenheit = 9/5 * c + 32  # Formula to convert Celsius to Fahrenheit
    return fahrenheit


# Function to convert  Fahrenheit to Celsius
def fahr(f):
    celsius = (f - 32) * 5/9  # Formula to convert Celsius to Fahrenheit
    return celsius


# call function convert Celsius to Fahrenheit
x = celc(20)

# call function convert Fahrenheit to Celsius
y = fahr(20)

# Celsius to Fahrenheit Output
print("degree Celsius is equal to " + str(x) + " degree Fahrenheit")

# Fahrenheit to Celsius Output
print("degree Fahrenheit is equal to " + str(y) + " degree Celsius")
