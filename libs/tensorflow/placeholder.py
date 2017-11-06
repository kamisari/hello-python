# vim: fileencoding=utf-8

import tensorflow as tf

def main():
    sess = tf.Session()

    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a + b
    print("adder_node:", adder_node)

    print("adder_node {a:9.9, b:0.1}:", sess.run(adder_node, {a: 9.9, b: 0.1}))
    print("adder_node {a:[1,3], b:[2,4]}:", sess.run(adder_node, {a: [1,3], b: [2, 4]}))
    #print("adder_node {a:[1,3,4], b:[2,4]}:", sess.run(adder_node, {a: [1,3,4], b: [2, 4]}))
    # err

if __name__ == '__main__':
    main()
