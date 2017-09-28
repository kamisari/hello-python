# vim: fileencoding=utf-8

import numpy as np

# maybe: maximum recursion depth exeption
# solution:
#import sys
#sys.setrecursionlimit(100000)

def merge(arr):
    if len(arr) <= 1:
        return arr
    div = len(arr)//2
    la = merge(arr[:div])
    lb = merge(arr[div:])
    return mergeList(la, lb, [])


def mergeList(a, b, l):
    if len(a) == 0 and len(b) == 0:
        return l
    if len(a) == 0:
        l.append(b[0])
        return mergeList(a, b[1:], l)
    if len(b) == 0:
        l.append(a[0])
        return mergeList(a[1:], b, l)
    if a[0] < b[0]:
        l.append(a[0])
        return mergeList(a[1:], b, l)
    else:
        l.append(b[0])
        return mergeList(a, b[1:], l)

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = merge(arr)
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

    print("mergeList:", mergeList([1,2,3,4],[1,2,3],[]))

if __name__ == '__main__':
    main()
