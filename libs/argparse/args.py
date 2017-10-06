# vim: fileencoding=utf-8

import argparse

def check_bool(args):
    print('check_bool')
    print('args.true:', args.true)
    print('args.false', args.false)

def check_string(args):
    print('check string')
    print(args.string+'/test')

def main():
    parser = argparse.ArgumentParser(description='accept arguments')
    parser.add_argument('--string', '-s', default='hello world', help='string')
    parser.add_argument('--true', action='store_true', help='bool true')
    parser.add_argument('--false', action='store_false', help='bool false')
    args = parser.parse_args()

    check_string(args)
    check_bool(args)

if __name__ == '__main__':
    main()
