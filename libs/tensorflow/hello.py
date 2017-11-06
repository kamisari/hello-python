# vim: fileencoding=utf-8

import tensorflow as tf

def main():
    hello = tf.constant('Hello, World!')
    sess = tf.Session()
    print(sess.run(hello))

if __name__ == '__main__':
    main()
