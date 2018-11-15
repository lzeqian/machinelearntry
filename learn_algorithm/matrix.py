import tensorflow as tf;
c=tf.constant([[1,2]]);
c1=tf.constant([[2],[3]]);
c2=tf.matmul(c,c1);
sess=tf.Session();
rt=sess.run(c2);
print(rt);

"""
矩阵相乘最重要的方法是一般矩阵乘积。它只有在第一个矩阵的列数（column）和第二个矩阵的行数（row）相同时才有意义 [1]  。
一般单指矩阵乘积时，指的便是一般矩阵乘积。一个m×n的矩阵就是m×n个数排成m行n列的一个数阵。由于它把许多数据紧凑的集中到了一起，
所以有时候可以简便地表示一些复杂的模型。
"""
with tf.Session() as sess:
    c=tf.constant([[1,2],[3,4]]);
    c1=tf.constant([[4,3],[1,2]]);
    c2=tf.matmul(c,c1);
    rt=sess.run(c2);
    print(rt);