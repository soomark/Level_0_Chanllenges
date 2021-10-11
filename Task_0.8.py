
def any_number(num):
    h = num // 60
    m = num % 60
    if h > 1 and m > 1:
        print(h, 'hours,', m, 'minutes')
    else:
        print(h, 'hour,', m, 'minute')


n = 133
any_number(n)
