class Targetnotfoundexception(Exception):
    pass

def binary_search(nums,target):
    if not isinstance(nums,list):
        raise TypeError('only list')
    try:
        i,r=0, len(nums)-1
        while i<=r:
            mid=(i+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i=mid + 1
            else:
                r = mid - 1
    except Exception:
        raise Targetnotfoundexception('target not found in the list')
    return -1