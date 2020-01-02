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
#参考：https://www.cnblogs.com/eczhou/p/5434996.html或者https://blog.csdn.net/zhu_wendao/article/details/89916869
arr = np.array([1, 2, 3, 100, 55])
# var 方差即各项-均值的平方求和后再除以N ，表示数据离平均数据的距离，表示数据的离散程度
print(np.var(arr))
print(np.sum(np.abs(arr - np.mean(arr)) ** 2) / len(arr))  # 等价代码
print(np.mean(abs(arr - arr.mean()) ** 2))  # 等价代码

# std：表示标准差，是var的平方根。
print(np.std(arr))
print(np.sqrt(np.var(arr)));

# cov：协方差 ,与var类似，但是除以(N-1)
print(np.cov(arr));
print(np.sum(np.abs(arr - np.mean(arr)) ** 2) / (len(arr) - 1))  # 等价代码
