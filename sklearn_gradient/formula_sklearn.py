import numpy as np;
import matplotlib.pyplot as plot
import sklearn.linear_model as lm;
np.random.seed(100);
x=np.random.rand(100);
X=x.reshape(-1,1);
#print(X)
y=x*3+4+np.random.rand(100);
plot.plot(x,y,"o");

lr=lm.SGDRegressor()
lr.fit(X,y);
print('回归系数：',lr.coef_)
print('偏差：',lr.intercept_ )
plot.plot(x,lr.intercept_ +lr.coef_*x)
plot.show();