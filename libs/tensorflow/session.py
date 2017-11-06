# vim: fileencoding=utf-8
# from tensorflow tutorial

import tensorflow as tf

def main():
    node1 = tf.constant(3.5, dtype=tf.float32)
    node2 = tf.constant(4.0)
    print(node1, node2)

    sess = tf.Session()
    print(sess.run([node1, node2]))

    node3 = tf.add(node1, node2)
    print("node3:", node3)
    print("sess.run(node3):", sess.run(node3))

if __name__ == '__main__':
    main()
