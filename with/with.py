#!/usr/bin/env python
# vim: fileencoding=utf-8


def with_file_open():
    with open('./text.txt', 'r') as text:
        print(text)
        c = 0
        for row in text:
            print(c, row)
            c += 1

def file_open():
    f = open('./text.txt', 'r')
    print(f)
    print(f.read())
    f.close()

def main():
    with_file_open()
    file_open()


if __name__ == '__main__':
    main()
