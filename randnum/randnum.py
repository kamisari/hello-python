# vim: fileencoding=utf-8

import random
import numpy

def basic():
    for x in range(10):
        print(x, ':', random.randint(0, 100))

def use_numpy():
    print(numpy.random.rand(10))
    print(numpy.random.uniform(0, 100, 10))
    print(numpy.random.randint(0, 100, 10))

def main():
    basic()
    use_numpy()

if __name__ == '__main__':
    main()
