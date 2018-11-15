import numpy as np
p=np.array([[-1,4],
            [-2,8]
            ]);
############求最大最小值#############
#获取整个矩阵的最大值 8
print(np.max(p))
print(np.max(p,axis=1)) #获取当前维度的最大值 二维就是每一行的最大值


print(np.argmax(p)) #从1维角度找到最大值的下标 8 在第4个位置也就是3上
print(np.argmax(p,axis=1)) #从2维角度获取最大值的下标 就是坐标 (1,1)
#获取最小值 -2
print(np.min(p))
print(np.argmin(p)) #获取最小值的位置 和 argmax一样
############求平均值#############
p1=np.array([[4,6],
            [3,1]
            ]);
print(np.mean(p1))  #4+6+3+1/4=3.5 也可以设置水平和垂直
print(np.mean(p1,axis=0)) #[3.5,3.5] 垂直
print(np.mean(p1,axis=1)) #[5,3] 水平

############方差#############
print(np.var(p1))
print(np.mean(abs(p1 - p1.mean())**2))

