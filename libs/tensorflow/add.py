# vim: fileencoding=utf-8

import tensorflow as tf

def main():
    sess = tf.Session()
    node1 = tf.constant(3.0, dtype=tf.float32)
    node2 = tf.constant(4.0)
    node3 = tf.constant(4)
    print("node1:", node1)
    print("node2:", node2)
    print("node3:", node3)

    node4 = tf.add(node1, node2)
    print("node4:", node4)
    print("sess.run(node4):", sess.run(node4))

    #node4 = tf.add(node1, node3)
    # err

    node5 = tf.add(node4, tf.constant(sess.run(node3), dtype=tf.float32))
    print("node5:", node5)
    print("sess.run(node5):", sess.run(node5))

    same_tfadd = node1 + node2
    print("same_tfadd:", same_tfadd)
    print("sess.run(same_tfadd):", sess.run(same_tfadd))

if __name__ == '__main__':
    main()
