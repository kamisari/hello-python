# vim: fileencoding=utf-8

# function name is lower_case_with_underscores

def default_value(n=0):
    print(n)
def default_value2(a, l=[]):
    '''Be careful'''
    l.append(a)
    print(l)
def default_value3(a, l=None):
    if l is None: l = []
    l.append(a)
    print(l)

def call2Default_values():
    print('call default_value:')
    default_value()
    default_value(1)
    print('call default_value2:')
    default_value2(0)
    default_value2(1)
    default_value2(2, [])
    print('call default_value3:')
    default_value3(0)
    default_value3(1)
    default_value3(2, [])

def main():
    '''this is documentation for this function
    see in CLI `pydoc ./def.py'
    '''
    pass

if __name__ == '__main__':
    main()
    call2Default_values()
