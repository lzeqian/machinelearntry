import numpy as np

p=np.array([n for n in range(1,10)]).reshape((3,3))
print(p.dtype)
print(p.shape)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(p);
'''
返回第1行
[1 2 3]
'''
print(p[0])
'''
返回第1行到第二行 但是不包括第二行 还是个二维数组
:表示当前维度   通过将由冒号分隔的切片参数(start:stop:step)直接提供给ndarray对象
,用于分割维度
[[1 2 3]]
'''
#表示一行到第二行 不包括第二行
print(p[0:1])
#表示从 第一行到第四行不包括4 每次跳 2步
print(p[0:3:2])


#返回第 1行 第2列的元素
print(p[0,2])
#返回第1行的第2-3个元素 都是包含开头不包含结尾
print(p[0,1:3])
#返回所有行和所有列
print(p[:,:])
#返回第二行和第三列所有元素
print(p[1:,2:])
# -1表示最后一行
print(p[-1])
# -表示最后一行和最后一列
print(p[-1,-1])
#找出所有大于5的
print(p[p>5])
#找出所有偶数
print(p[p%2==0])
#查找所有的数组 取反
a=np.array([1,2,np.nan,np.nan])
print(a[~np.isnan(a)])

