# Function calculating the area of a triangle using Herons formula
def area_calculation(x, p, u):
    # calculate the semi-perimeter
    s = (x + p + u) / 2

    # calculate the area
    area = (s * (s - x) * (s - p) * (s - u)) ** 0.5
    print('Area of a triangle is: ' + str(area))


x = input('Enter your 1st value: ')
x = int(x)
p = input('Enter your 2nd value: ')
p = int(p)
u = input('Enter your 3rd value: ')
u = int(u)
area_calculation(x, p, u)
