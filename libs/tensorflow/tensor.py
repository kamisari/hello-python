# vim: fileencoding=utf-8
# from tensorflow tutorial

import tensorflow as tf

def main():
    node1 = tf.constant(3.0, dtype=tf.float32)
    node2 = tf.constant(4.0)
    print(node1, node2)

if __name__ == '__main__':
    main()
