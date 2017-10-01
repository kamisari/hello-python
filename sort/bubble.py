# vim: fileencoding=utf-8

import numpy as np

def bubblesort(arrOrigin):
    arr = arrOrigin.copy()
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = bubblesort(arr)
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

if __name__ == '__main__':
    main()
