

def bubbleSort(arr):
    n = len(arr)
    if n == 1:
        return
    
    swapped = True
    for i in range(n-1):
        if not swapped:
            break
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr