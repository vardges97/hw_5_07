def fib(n):
    try:
        if n<0:
            print('wrong input >:(')

        elif n == 0:
            return 0

        elif n==1 or n==2:
            return 1

        else:
            return fib(n-2) + fib(n-1)
    except TypeError:
        raise TypeError('given number must be integer')

print(fib(6))