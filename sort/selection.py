# vim: fileencoding=utf-8

import numpy as np

def selection_sort(arrOrigin):
    arr = arrOrigin.copy()
    for i in range(len(arr)):
        minIndex = i
        for j in range(len(arr[i:])):
            if arr[minIndex] > arr[i+j]:
                minIndex = i+j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = selection_sort(arr)
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

if __name__ == '__main__':
    main()
