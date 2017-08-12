# vim: fileencoding=utf-8

def typeList():
    print('typeList():')
    squares = [1, 4, 9, 16, 25]
    for x in squares:
        print(x)
    print('append,36')
    squares.append(36)
    print('squares=',squares)
    cp = squares[1:]
    print(cp, squares)
    print('len: cp squares', len(cp), len(squares))


def main():
    typeList()

if __name__ == '__main__':
    main()
