import numpy as np


p=np.array([[-1,4],
            [-2,8]
            ]);
p1=np.array([[4,6],
            [3,1]
            ]);
#矩阵乘法是将各个位置的值相乘
p3=p*p1;
print(p3);
print(np.multiply(p,p1)) #等价于上面
#点乘法 是将行和列相乘
'''
第一行的任意数字和第一列的任意数字累加
-1*4+-4*3=8  最后在第一行
第一行的任意数字和第二列的任意数字累加
-1*6+4*1=-2 在第一行

接下来第二行和第一列和第二列点乘 放在第二列
'''
print(np.dot(p,p1));#两个数组的点积，即元素对应相乘。 dot通用所有数组
print(np.matmul(p,p1))#两个数组的矩阵积

p=np.array([1,2]);
p1=np.array([2,3]);
print(np.vdot(p,p1))#两个向量的点积  1*2+2*3=8
print(np.inner(p,p1))




