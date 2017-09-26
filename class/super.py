# vim: fileencoding=utf-8

class Dog(object):
    def __init__(self, name):
        self.name = name

class BigDog(Dog):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

def main():
    d = Dog("Doggy")
    print(d, d.name)

    bd = BigDog("BDoggy", "NextOne")
    print(bd, bd.name)

if __name__ == '__main__':
    main()
