def bubbleSort(arr):
        n = len(arr)
        swapped = False

       
        for i in range(n-1):
            for j in range(0, n-i-1):

               
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j +1] = arr[j + 1], arr[j]

            if not swapped:
              
                return


def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
          
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        
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


def cycleSort(array):
  writes = 0
   

  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
     
   
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
     
  
    if pos == cycleStart:
      continue
     
  
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
     
   
    while pos != cycleStart:
       
 
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
       

      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
 
        heapify(arr, n, largest)
 
 

 
def heapSort(arr):
    n = len(arr)
 

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
  

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
           
            if array[j] < array[min_index]:
                min_index = j
        
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def shellSort(array):
    n = len(array)
  
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2