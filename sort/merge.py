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
    return merge_list(la, lb, [])


def merge_list(a, b, l):
    if len(a) == 0 and len(b) == 0:
        return l
    if len(a) == 0:
        l.append(b[0])
        return merge_list(a, b[1:], l)
    if len(b) == 0:
        l.append(a[0])
        return merge_list(a[1:], b, l)
    if a[0] < b[0]: # reverse: '>'
        l.append(a[0])
        return merge_list(a[1:], b, l)
    else:
        l.append(b[0])
        return merge_list(a, b[1:], l)

def main():
    arr = np.random.randint(0, 1000, 10)
    print("befor:", arr, "arr")
    afterarr = merge(arr)
    print("after:", afterarr, "afterarr")
    print("check:", arr, "arr")

    print("merge_list:", merge_list([1,2,3,4],[1,2,3],[]))

if __name__ == '__main__':
    main()
