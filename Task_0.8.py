# Function converts any number to hour and minutes
def any_number(num):
    h = num // 60
    m = num % 60

    print(h, 'hour,', m, 'minute')


n = 61
any_number(n)
