# vim: fileencoding=utf-8


def iterator():
    print('\niterator()')
    words = ['c', 'python', 'go', 'ruby']
    for w in words:
        print('w = ', w, len(w))

def iterator_limit10():
    print('\niterator_limit10()')
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

def iterator_copy():
    print('\niterator_copy()')
    words = ['c', 'python', 'go', 'ruby']
    print('before: words = ', words)
    for w in words[:]:
        print('w = ', w, len(w))
        if len(w) > 5:
            words.insert(0, w)
    print('after: words = ', words, '\n')

def iterator_copy_slice():
    print('\niterator_copy()')
    words = ['c', 'python', 'go', 'ruby']
    print('words = ', words)
    print('slice[1:3]')
    for w in words[1:3]:
        print('w = ', w, len(w))

def for_range():
    print('\nfor_range()')
    print('range 10')
    for i in range(10):
        print('  ', i)
    print('range 0 10 3')
    for i in range(0, 10, 3):
        print('  ', i)
    print('range -10 -100 -30')
    for i in range(-10, -100, -30):
        print('  ', i)

def len_range():
    print('\nlen_range()')
    words = ['c', 'python', 'go', 'ruby']
    for i in range(len(words)):
        print(i, words[i])

def for_else():
    print('\nfor_else()')
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else: # loop fell through
            print(n, 'is a prime number')

def loop_continue():
    print('\nloop_continue()')
    for i in range(10):
        continue
        print(i) # unreachable
    print('exit unreachable loop')

def for_range():
    print('\nfor_range()')
    arr = [0,1,2,3,4,5]
    for i in range(len(arr)):
        print(i, arr[i])
    print('override')
    for i in range(len(arr)):
        print(i, arr[i])
        i += 10
        print("after += :", i)

def main():
    iterator()
    iterator_limit10()
    iterator_copy()
    iterator_copy_slice()
    for_range()
    len_range()
    for_else()
    loop_continue()
    for_range()


if __name__ == '__main__':
    main()
