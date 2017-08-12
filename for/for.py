# vim: fileencoding=utf-8


def iterator():
    print('\niterator()')
    words = ['c', 'python', 'go', 'ruby']
    for w in words:
        print('w = ', w, len(w))

def iteratorLimit10():
    print('\niteratorLimit10()')
    words = ['c', 'python', 'go', 'ruby']
    print('before: words = ', words)
    count = 0
    for w in words:
        count = count + 1
        if count > 10:
            break
        print('w = ', w, len(w))
        if len(w) > 5:
            words.insert(0, w)
    print('after: words = ', words, '\n')

def iteratorCopy():
    print('\niteratorCopy()')
    words = ['c', 'python', 'go', 'ruby']
    print('before: words = ', words)
    for w in words[:]:
        print('w = ', w, len(w))
        if len(w) > 5:
            words.insert(0, w)
    print('after: words = ', words, '\n')

def iteratorCopySlice():
    print('\niteratorCopy()')
    words = ['c', 'python', 'go', 'ruby']
    print('words = ', words)
    print('slice[1:3]')
    for w in words[1:3]:
        print('w = ', w, len(w))

def forRange():
    print('\nforRange()')
    print('range 10')
    for i in range(10):
        print('  ', i)
    print('range 0 10 3')
    for i in range(0, 10, 3):
        print('  ', i)
    print('range -10 -100 -30')
    for i in range(-10, -100, -30):
        print('  ', i)

def lenRange():
    print('\nlenRange()')
    words = ['c', 'python', 'go', 'ruby']
    for i in range(len(words)):
        print(i, words[i])

def forElse():
    print('\nforElse()')
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else: # loop fell through
            print(n, 'is a prime number')

def loopContinue():
    print('\nloopContinue()')
    for i in range(10):
        continue
        print(i) # unreachable
    print('exit unreachable loop')


def main():
    iterator()
    iteratorLimit10()
    iteratorCopy()
    iteratorCopySlice()
    forRange()
    lenRange()
    forElse()
    loopContinue()


if __name__ == '__main__':
    main()
