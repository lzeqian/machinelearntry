import numpy as np;
import matplotlib.pyplot as plot;
import sklearn.linear_model as lm;
import sklearn.datasets as ds;
import sklearn.model_selection as ms;

bd=ds.load_boston();
#获取波士顿房价的所有特征数据
data=bd.data;
#获取每行特征对应的房价
label=bd.target;
#将数据拆分成80%的训练数据  20%的测试数据
xtrain,xtest,ytrain,ytest=ms.train_test_split(data,label,test_size=0.2,random_state=10)
xtrain=xtrain[ytrain<50]
ytrain=ytrain[ytrain<50]
lr=lm.LinearRegression();
lr.fit(xtrain,ytrain);
#系数也就是斜率
np.set_printoptions(suppress=True) #不使用科学计数法
print("所有的系数:");
print(lr.coef_)
#截距
print(lr.intercept_)
print(np.argsort(lr.coef_))



