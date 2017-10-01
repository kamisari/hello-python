# vim: fileencoding=utf-8


# TODO: impl

import numpy as np

# zero baseed heap in array
# parent:      (index-1)//2
# child left:  index*2+1
# child right: index*2+2

def heap(arr):
    return arr

def makeHeap(arr):

    #i = 0
    #index = i
    #x = arr[index]
    #lam = lambda: x < arr[(index-1)//2]
    #print(lam())

    for i in range(len(arr)):
        index = i
        x = arr[index]
        print(i, ": before", arr)
        while index > 0 and x < arr[(index-1)//2]: # reverse  x > arr[(index-1)//2]
            print("swapp: index=", index, "x=", x, "parent=", arr[(index-1)//2])
            arr[index] = arr[(index-1)//2]
            index = (index-1)//2
        arr[index] = x
        print(i, ": after ", arr)
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = heap(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

    print("makeHeap:", makeHeap(arr))

if __name__ == '__main__':
    main()
