# vim: fileencoding=utf-8

import os
import tensorflow as tf

def main():
    sess = tf.Session()

    node1 = tf.constant(.3)
    node2 = tf.constant(.4)
    node3 = tf.add(node1, node2)
    print("sess.run(node3):", sess.run(node3))

    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder = a + b
    print("adder:", sess.run(adder, {a: 10, b:.1}))

    logdir = os.path.dirname(os.path.abspath(__file__))+"/logdir"
    file_writer = tf.summary.FileWriter(logdir,  sess.graph)

if __name__ == '__main__':
    main()
