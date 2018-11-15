import numpy as np;

print(np.add(1,2));
#产生一个2维数据  2行散列 值全部是1
n=np.ones((2,3));
print(n)
#产生一个2维数据  3行4列 值全部是0
z=np.zeros((3,4));
print(z);
#产生一个矩阵 5X5 对角线是1 其他是0
e=np.eye(5);
print(e);
