import tensorflow as tf;

#常量定义
c=tf.constant("hello world");
sess=tf.Session();
rt=sess.run(c);
print(rt);

#tensorflow常量定义 变量定义不会被运行 必须通过session
c=tf.constant([1,2,3,4,5]);
sess=tf.Session();
rt=sess.run(c);
print(rt);
#将某个数组转换成 3行2列
c1=tf.constant([1,2,3,4,5],shape=[3,2]);
sess=tf.Session();
rt=sess.run(c1);
print(rt);
#将创建 3行2列 所以值都是10
c1=tf.constant(10,shape=[3,2]);
sess=tf.Session();
rt=sess.run(c1);
print(rt);





