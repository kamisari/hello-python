# vim: fileencoding=utf-8

import numpy as np

def insertion(arr, n=1):
    for i in range(0, len(arr), n):
        v = arr[i]
        j = i-n
        while j > -1 and v < arr[j]:
            arr[j+n] = arr[j]
            j -= n
        # fill in the blank
        arr[j+n] = v
    return arr

def shell(arr, n=1):
    for i in range(n, 0, -1):
        print("\t", "shell: n:", i, arr)
        arr = insertion(arr, i)
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = insertion(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")
    print("shell:", shell(arr.copy(), 4), "n:", 4)

if __name__ == '__main__':
    main()
