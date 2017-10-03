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

def make_heap(arr, end=None):
    if end == None:
        end = len(arr)
    for i in range(end):
        index = i
        x = arr[index]
        #if index > 0:
        #    print("node=", index, "parent=", (index-1)//2)
        while index > 0 and x > arr[(index-1)//2]: # reverse  x < arr[(index-1)//2]
            #print("arr  :", arr, "swapp:", x, arr[(index-1)//2])
            arr[index] = arr[(index-1)//2]
            index = (index-1)//2
        arr[index] = x
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = heap(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

if __name__ == '__main__':
    main()
