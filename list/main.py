# vim: fileencoding=utf-8

def type_list():
    print('type_list():')
    squares = [1, 4, 9, 16, 25]
    for x in squares:
        print(x)
    print('append,36')
    squares.append(36)
    print('squares=',squares)
    cp = squares[1:]
    print(cp, squares)
    print('len: cp squares', len(cp), len(squares))


def slice():
    l = [1,2,3,4]
    print(l)
    print("l[0:]", l[0:])
    print("l[1:]", l[1:])
    print("l[:0]", l[:0])

    l2 = [1]
    print("l2[0:]", l2[0:])
    print("l2[1:]", l2[1:])

def main():
    type_list()
    print("slice")
    slice()

if __name__ == '__main__':
    main()
