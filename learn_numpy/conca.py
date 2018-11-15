import numpy as np

p=np.arange(1,10).reshape((3,3));
p1=np.array([[-1,4,6],
    [-2,8,11],
    [8,3,1]
    ]);
print(p);
print(p1);

#合并矩阵 默认是在水平方向合并
print(np.concatenate((p,p1)));
print(np.hstack((p,p1))) #水平合并
# 0表示1维水平方向 1表示二维方向上 也就是垂直方向
print(np.concatenate((p,p1),axis=1));
print(np.vstack((p,p1))) #垂直合并
