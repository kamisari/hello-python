# vim: fileencoding=utf-8

def add(x, y):
    print('add():', x+y)

def subtract(x, y):
    print('subtract():', x-y)

def multiply(x, y):
    print('multiply():', x*y)

def divide(x, y):
    print('divide():', x/y)

def discard_part(x, y):
    print('discard_part():', x//y)

def surplus(x, y):
    print('surplus():', x%y)

def squared(x, y):
    print('squared():', x**y)


def check_div():
    print("check_div():")
    for i in range(11):
        print(i)
        for j in range(1,11):
            print("j:", j, "result:",  i//j)

def main():
    add(4,2)
    subtract(4,2)
    multiply(4,2)
    divide(5,2)
    discard_part(5,2)
    surplus(5,2)
    squared(4,2)

if __name__ == '__main__':
    main()
    check_div()
