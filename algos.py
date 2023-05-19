

def bubbleSort(arr):
        n = len(arr)
        swapped = False

        # Traverse through all array elements
        for i in range(n-1):
            for j in range(0, n-i-1):

                # Swap if the element found is greater
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j +1] = arr[j + 1], arr[j]

            if not swapped:
                # if we haven't needed to make a single swap, we can just exit the main loop.
                return


def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        arr[j + 1] = key
 

def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p - 1)
        quickSort(arr, p + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i
