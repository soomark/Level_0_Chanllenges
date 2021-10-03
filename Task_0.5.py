# Function calculating the area of a triangle using Herons formula
def area_calculation(x, p, u):
    # calculate the perimeter
    s = (x + p + u) / 2

    # calculate the area
    area = (s * (s - x) * (s - p) * (s - u)) ** 0.5
    return area


# User input values
a = int(input("Enter 1st length: "))
b = int(input("Enter 2nd length: "))
c = int(input("Enter 3rd length: "))

# call function
area_of_triangle = area_calculation(a, b, c)

# Output
print("Area of Triangle is " + str(area_of_triangle))
