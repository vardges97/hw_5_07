db={}
def factoral(num:int):

    try:
        if (num==1 or num==0):
            return 1
        elif num in db:
            return db[num]

        res = (num*factoral(num-1))
        db[num]=res
    except TypeError:
        raise TypeError("argument must be integer")
    except RecursionError:
        raise RecursionError('Recursion limit reached')
    return res

print(factoral(40))
