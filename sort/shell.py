# vim: fileencoding=utf-8

import numpy as np

def insertion(arr, interval=1):
    for i in range(0, len(arr), interval):
        v = arr[i]
        j = i-interval
        while j > -1 and v < arr[j]:
            arr[j+interval] = arr[j]
            j -= interval
        # fill in the blank
        arr[j+interval] = v
    return arr

def shell(arr, interval=1):
    for i in range(interval, 0, -1):
        print("\t", "shell: interval:", i, arr)
        arr = insertion(arr, i)
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = insertion(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")
    print("shell:", shell(arr.copy(), 4))

if __name__ == '__main__':
    main()
