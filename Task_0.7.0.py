# Function to convert Celsius to Fahrenheit
def celc(c):
    fahrenheit = 9/5 * c + 32  # Formula to convert Celsius to Fahrenheit
    print('%.2f degree Celsius is equal to %0.2f degree Fahrenheit' % (c, fahrenheit))


c = input('Input the Celsius value: ')
c = float(c)
celc(c)

