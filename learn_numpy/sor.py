import numpy as np
#默认按照行排序
p=np.array([[-1,8],
            [4,-2]
            ]);

print(np.sort(p))
#按照列排序
print(np.sort(p,axis=0))


#自定义对象数据类型 参考http://www.runoob.com/numpy/numpy-dtype.html 按照字段排序
mtype=np.dtype([('name','S'),('age',int)])
p=np.array([('zs',20),('ww',60),('zl',30)],dtype=mtype)
print(np.sort(p,order='age'))

p=np.array([3,1,2])
#argsort() 函数返回的是数组值从小到大的索引值。
print(np.argsort(p))
#逆序
print(np.sort(p)[::-1])



