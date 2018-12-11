import numpy as np;
import matplotlib.pyplot as plot
np.random.seed(100);
x=np.random.rand(100);
X=x.reshape(-1,1);
#print(X)
y=x*3+4+np.random.rand(100);
plot.plot(x,y,"o");


#使用梯度下降法拟合这个函数

"""
 获取损失函数的y值
 sum(y-t0-t1*x1-t2*x2 -.....tn*xn)**2
"""
def j(x,y,theta):
    #return np.sum((y-x.dot(theta))**2)/len(y)
    return np.sum((y-(theta[0]+theta[1]*x[:,1]))**2)/len(y);

"""
计算所有theta的梯度 
 t0=sum(2(y-tx.*x)*-1)
 t1=sum(2(y-tx.*x)*-x1)
"""

def dj(x,y,theta):
   djArr=np.empty((len(theta)))
   djArr[0]=np.sum(2*(x.dot(theta)-y));
   for i in range(1,len(theta)):
       djArr[i] = np.sum(2 * (x.dot(theta) - y)*x[:,i]);
   return 2/len(x)*djArr;

"""
梯度下降获取最佳的值
"""
x_b=np.hstack((np.ones((len(x),1)),X));
init_theta=np.array([0.1,0.5]);
eta=0.01;
while True:
    jr=j(x_b,y,init_theta) #获取损失函数的y值
    djr=dj(x_b,y,init_theta) #获取梯度值
    init_theta=init_theta-eta*djr;#让theta按梯度下降
    if(np.all(np.abs(djr)<=1e-5)):
        break;
#打印获取到的两个的theta的值
print(init_theta);
#打印图x和通过theta获取的y值
plot.plot(x,init_theta[0]+init_theta[1]*x)
plot.show();
