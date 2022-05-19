

def fibonacci(n):
    """
    This is a recursive function that starts with 0 and 1 and adds the previous two
    numbers to get the next number.
    It returns the nth number in the Fibonacci sequence
    """
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    This is a recursive function that starts with 2 and 1 and adds the previous two
    numbers to get the next number.
    It returns the nth number in the Lucas sequence
    """
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, num_zero=0, num_one=1):
    """
    This is a recursive function that that starts with and two numbers
    specified by the user and adds the previous two numbers to get the next number.
    It returns the nth number in the Fibonacci, Lucas or other kind of sequence
    """
    if n < 0:
        return 'incorrect input'
    elif n == 0:
        return num_zero
    elif n == 1:
        return num_one
    else:
        return sum_series(n-1, num_zero, num_one) + sum_series(n-2, num_zero, num_one)


