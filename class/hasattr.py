# vim: fileencoding=utf-8

class NotHave:
    pass

class Have:
    def have():
        pass

def main():
    nh = NotHave()
    print(hasattr(nh, 'have'))
    h = Have()
    print(hasattr(h, 'have'))

if __name__ == '__main__':
    main()
