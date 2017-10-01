#!/usr/bin/env python
# vim: fileencoding=utf-8


def main():
    print('hello world')
    print('hello ', end=',,,')
    print('world')
    print('up\ndown')
    print(r'up\ndown')
    s = '''
multi line
hello world
'''
    print(s)
    print('dock', 'hello''world')
    print('hi'*2)

if __name__ == '__main__':
    main()
