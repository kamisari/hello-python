# vim: fileencoding=utf-8

def fib(x):
    print('fib():')
    a, b = 0, 1
    while b < x:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib_range(x):
    print('fib_range():')
    a, b = 0, 1
    for i in range(x):
        print(b, end=' ')
        a, b = b, a+b
    print()

def check_the_none():
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
    fib_range(100)

    print('\nCheck the None')
    print(check_the_none())
    print(check_the_none()==None)
    print()

    print(fib2(10))
    print(fib2())

if __name__ == '__main__':
    main()
