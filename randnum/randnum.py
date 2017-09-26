# vim: fileencoding=utf-8

import random
import numpy

def basic():
    for x in range(10):
        print(x, ':', random.randint(0, 100))

def useNumpy():
    print(numpy.random.rand(10))
    print(numpy.random.uniform(0, 100, 10))
    print(numpy.random.randint(0, 100, 10))

def main():
    basic()
    useNumpy()

if __name__ == '__main__':
    main()
