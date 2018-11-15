import numpy as np
p=np.array([[-1,4,5],
            [-2,8,6]
            ]);
#将第一行转换成第一列 其他行转换其他列
p1=p.transpose();
print(p1);
print(p.T);#等价于上面


#必须是方形矩阵才能求逆矩阵
a = np.array([[1,2],[4,5]])
print(np.linalg.inv(a))