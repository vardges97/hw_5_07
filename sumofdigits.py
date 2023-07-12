def sumof(n:int):
    if not isinstance(n,int):
        raise TypeError('given number must be an integer')
    return 0 if n == 0 else int(n % 10) + sumof(int(n/10))
n = 2222
print(sumof(n))