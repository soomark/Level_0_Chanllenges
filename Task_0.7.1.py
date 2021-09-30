# Function to convert  Fahrenheit to Celsius
def celc(c):
    celsius = (c - 32) * 5/9  # Formula to convert Celsius to Fahrenheit
    print('%.2f degree Fahrenheit is equal to %0.2f degree Celsius' % (c, celsius))


c = input('Input the Fahrenheit value: ')
c = float(c)
celc(c)