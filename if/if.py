# vim: fileencoding=utf-8


def main():
    x = int(input("input integer:>"))
    if x < 0:
        x = 0
        print("negative value is invalid")
    elif x == 0:
        print("zero")
    elif x == 1:
        print("single")
    else:
        print("x is", x)

if __name__ == '__main__':
    main()
