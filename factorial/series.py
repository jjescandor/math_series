def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(5))