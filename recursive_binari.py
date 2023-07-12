class Targetnotfoundexception(Exception):
    pass

def binary_recursive(arr,target,low,high):
    if low > high:
        raise Targetnotfoundexception("target not in the list")
    if not isinstance(arr,list):
        raise TypeError('only lists')
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid]==target:
        return mid

    if arr[mid]>target:
        return binary_recursive(arr,target,low,mid-1)
    else:
        return binary_recursive(arr,target,mid+1,high)