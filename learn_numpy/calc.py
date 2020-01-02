import numpy as np


p=np.array([[-1,4],
            [-2,8]
            ]);
p1=np.array([[4,6],
            [3,1]
            ]);
#矩阵乘法是将各个位置的值相乘
p3=p*p1;
print("-------------------")
print("输出->p*p2")
print(p3);
print("-------------------")
print("输出->np.multiply(p,p1)")
print(np.multiply(p,p1)) #等价于上面
print("-------------------")
#点乘法 是将行和列相乘
'''
第一行的任意数字和第一列的任意数字累加
-1*4+-4*3=8  最后在第一行
第一行的任意数字和第二列的任意数字累加
-1*6+4*1=-2 在第一行

接下来第二行和第一列和第二列点乘 放在第二列
点乘物理意义求两个向量夹角 https://www.cnblogs.com/gxcdream/p/7597865.html，向量模https://baike.baidu.com/item/%E5%90%91%E9%87%8F%E7%9A%84%E6%A8%A1/2073854?fr=aladdin
'''
print("输出点乘->np.dot(p,p1)")
print(np.dot(p,p1));#两个数组的点积，即元素对应相乘。 dot通用所有数组
print("-------------------")
print(np.matmul(p,p1))#两个数组的矩阵积

p=np.array([1,2]);
p1=np.array([2,3]);
print(np.vdot(p,p1))#两个向量的点积  1*2+2*3=8
print(np.inner(p,p1))


print(np.array([1,2]).dot(np.array([3,4])))



