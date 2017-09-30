# vim: fileencoding=utf-8


# TODO: impl

import numpy as np

def heap(arr):
    return arr

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = heap(arr.copy())
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

if __name__ == '__main__':
    main()
