def factoral(n):
    if (n==1 or n==0):
        return 1

    else:

        return (n*factoral(n-1))


print(factoral(6))
