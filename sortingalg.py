def bubblesort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

def insertion(arr):

    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
        return arr