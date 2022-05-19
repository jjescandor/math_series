

def fibonacci(n):
    if n < 0:
        print('incorrect input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, num_zero=0, num_one=1):
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return num_zero
    elif n == 1:
        return num_one
    else:
        return sum_series(n-1, num_zero, num_one) + sum_series(n-2, num_zero, num_one)


