# vim: fileencoding=utf-8


import numpy as np

# zero baseed heap in array
# parent:      (index-1)//2
# child left:  index*2+1
# child right: index*2+2

def heap(arr):
    for i in range(len(arr)-1, -1, -1):
        make_heap(arr, i+1)
        arr[0], arr[i], = arr[i], arr[0]
    return arr

def upheap(arr, x, index=None):
    if index is None:
        arr.append(x)
        index = len(arr)-1
    while index > 0 and x < arr[(index-1)//2]:
        arr[index] = arr[(index-1)//2]
        index = (index-1)//2
    arr[index] = x

def make_heap(arr, end=None):
    if end == None:
        end = len(arr)
    index = 0
    parent = lambda: (index-1)//2
    for index in range(end):
        x = arr[index]

        #if index > 0:
        #    print("node=", index, "parent=", parent())

        ### upheap ###
        while index > 0 and x > arr[parent()]: # reverse  x < arr[parent()]
            #print("arr  :", arr, "swapp:", x, arr[parent()])
            arr[index] = arr[parent()]
            index = parent()
        arr[index] = x
    return arr

def is_heap(arr):
    for i in range(1, len(arr)):
        if arr[(i-1)//2] > arr[i]:
            return False
    return True

def main():
    arr = list(np.random.randint(0, 1000, 10))
    print("befor:", arr, "arr")
    afterarr = heap(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")
    print(is_heap(arr), is_heap(afterarr))
    upheap(afterarr, 0)
    print("upheap(afterarr, 0):", afterarr)
    print(is_heap(afterarr))

if __name__ == '__main__':
    main()
