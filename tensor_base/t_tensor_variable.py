import tensorflow as tf;

#变量定义 默认指定初始值 指定张量名字
c=tf.Variable(3,dtype=tf.int8,name="c1");
print(c);
#sess=tf.Session();
#rt=sess.run(c.initializer);
#print(rt);

#placehoder占位符用法
c=tf.placeholder(dtype=tf.float32,shape=(2,2));
cc=tf.matmul(c,c);
arg=[[1,2],[4,5]];
print(tf.Session().run(cc,feed_dict={c:arg}));



