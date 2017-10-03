# vim: fileencoding=utf-8

# TODO:

def main():
    show = lambda i, x:(
            (print(i)),
            (print(str(i),":", str(x))),
            (print(str(i),":", repr(x))),
        )
    show(0, main)
    num = 100
    show(1, num)
    div = 4/7
    show(2, div)
    show(3, (("hi", 1/2),("hello", 3/4)))

if __name__ == '__main__':
    main()
