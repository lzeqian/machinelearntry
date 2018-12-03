import numpy as np;
import matplotlib.pyplot as plot;
import sklearn.linear_model as lm;
import sklearn.datasets as ds;
import sklearn.model_selection as ms;
"""
  返回一个json数据（结构）
    data表示房价数据
    target
    feature_names 表示每个列的字段名称
    DESCR 是描述信息
    filename：存储的数据文件的位置
  关于该数据所有字段：  
    CRIM：城镇人均犯罪率。
    ZN：住宅用地超过 25000 sq.ft. 的比例。   
    INDUS：城镇非零售商用土地的比例。   
    CHAS：查理斯河空变量（如果边界是河流，则为1；否则为0）    
    NOX：一氧化氮浓度。  
    
    AGE：1940 年之前建成的自用房屋比例。   
    DIS：到波士顿五个中心区域的加权距离。   
    RAD：辐射性公路的接近指数。
    TAX：每 10000 美元的全值财产税率。   
    PTRATIO：城镇师生比例。    
    B：1000（Bk-0.63）^ 2，其中 Bk 指代城镇中黑人的比例。  
    LSTAT：人口中地位低下者的比例。 
    MEDV：自住房的平均房价，以千美元计。
    target是房价 以千美元计
"""
bd=ds.load_boston();
#获取波士顿房价的所有特征数据
data=bd.data;
#获取每行特征对应的房价
label=bd.target;
#为了演示简单线性回归 获取一个特征
#RM：住宅平均房间数。
nox=data[: ,5:6]
#将数据拆分成80%的训练数据  20%的测试数据
xtrain,xtest,ytrain,ytest=ms.train_test_split(nox,label,test_size=0.2,random_state=10)
xtrain=xtrain[ytrain<50]
ytrain=ytrain[ytrain<50]
#将 [[4],[2]]这样的特征矩阵转换成 [4,2]这样的向量
plot.scatter(xtrain[:,-1],ytrain,c="red")
plot.show();

#创建线程回归的类
lr=lm.LinearRegression();
lr.fit(xtrain,ytrain);
#系数也就是斜率
print(lr.coef_)
#截距
print(lr.intercept_)
plot.scatter(xtrain[:,-1],ytrain,c="red")
#绘制 80%的真实数据
plot.plot(xtrain[:,-1],xtrain[:,-1]*lr.coef_+lr.intercept_);
plot.show();



