# vim: fileencoding=utf-8

def fib(x):
    print('fib():')
    a, b = 0, 1
    while b < x:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fibRange(x):
    print('fibRange():')
    a, b = 0, 1
    for i in range(x):
        print(b, end=' ')
        a, b = b, a+b
    print()

def checkTheNone():
    print(end='')

def fib2(x=20):
    print('fib2')
    result = []
    a, b = 0, 1
    while a < x:
        result.append(a)
        a, b = b, a+b
    return result

def main():
    fib(1000)
    fibRange(100)

    print('\nCheck the None')
    print(checkTheNone())
    print(checkTheNone()==None)
    print()

    print(fib2(10))
    print(fib2())

if __name__ == '__main__':
    main()
