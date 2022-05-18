

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


def sum_series(n, num_zero = 0, num_one=1, ):
    if num_zero == 0 and num_one == 1:
        return fibonacci(n)
    elif num_zero == 2 and num_one == 1:
        return lucas(n)


