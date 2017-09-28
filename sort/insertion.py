# vim: fileencoding=utf-8

import numpy as np

def insertion(arrOrigin):
    arr = arrOrigin.copy()
    for i in range(1, len(arr)):
        v = arr[i]
        j = i-1
        # arr[i] = blank
        while j != -1 and v < arr[j]:
            print(i, "j:", j, v, "<", arr[j])
            arr[j+1] = arr[j]
            j -= 1
        # fill in the blank
        arr[j+1] = v
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = insertion(arr)
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

if __name__ == '__main__':
    main()
