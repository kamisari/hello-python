# vim: fileencoding=utf-8

import sys
import module
from module2 import fun
#from module2 import fun2

def main():
    print('sys.path:', sys.path)
    print('module name:', module.__name__)
    print('module.global_variable:', module.global_variable)
    module.hello()
    fun()
    try:
        fun2()
    except NameError:
        print('NameError exception')
        print('not found fun2()')


if __name__ == '__main__':
    main()
