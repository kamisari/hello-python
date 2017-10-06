# vim: fileencoding=utf-8

import numpy as np

def main():
    with np.load('./test.npz') as test:
        print('test:', test)
        print(type(test))
        for x in dir(test):
            print(x)
    with np.load('./train.npz') as train:
        print('train:', train)

if __name__ == '__main__':
    main()
