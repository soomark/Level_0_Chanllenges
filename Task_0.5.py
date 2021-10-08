# Function calculating the area of a triangle using Herons formula
def area_calculation(x, p, u):
    # calculate the perimeter
    s = (x + p + u) / 2

    # calculate the area
    area = (s * (s - x) * (s - p) * (s - u)) ** 0.5
    return area


# call function
area_of_triangle = area_calculation(10, 10, 10)

# Output
print(f'Area of Triangle is {area_of_triangle}')
