import numpy as np
#X定义域，X中的值:1就是原像x
X=np.array([1,2,3,4])
#Y定义域，Y中的值:2就是像y,可以理解为y是一个变量可以代表 2 4 6 8任意一个数，Y是整个集合
#
Y=np.array([2,4,6,8,10])
# f(x)表示映射 X和Y的映射关系就是x的两倍就是y,其中Rf值域是最终算出来的 [2 4 6 8] 和集合Y完全映射就是满射，显然Y中有个10没有满射
# 但是每个x都有一个对应y，满足单射条件
y=2*X;
print(y);