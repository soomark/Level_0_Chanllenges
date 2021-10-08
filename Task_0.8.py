# Function converts any number to hour and minutes
def any_number(num):
    h = num // 60
    m = num % 60

    print(h, 'hours,', m, 'minutes')


n = 60
any_number(n)
