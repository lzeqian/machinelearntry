import numpy as np;
import matplotlib.pyplot as plot;

def setXY():
    # 获取当前坐标轴对象
    ax = plot.gca()

    # 将垂直坐标刻度置于左边框
    ax.yaxis.set_ticks_position('left')
    # 将水平坐标刻度置于底边框
    ax.xaxis.set_ticks_position('bottom')
    # 将左边框置于数据坐标原点
    ax.spines['left'].set_position(('data', 0))
    # 将底边框置于数据坐标原点
    ax.spines['bottom'].set_position(('data', 0))

    # 将右边框和顶边框设置成无色
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
#演示 计算函数 y=(x-2)**2+2的 最小值y所在x的位置
# 可以知道的是 任何数的平方都应该大于0 所有 x=2时 y最小=2
# 通过t度下降法来预算
setXY();
x=np.linspace(-10,10,100);
plot.plot(x,(x-2)**2+2)
"""
 获取每一个点的梯度 
"""
def gradient(x):
    return 2*(x-2);
"""
获取每个点的dy值
"""
def dy(x):
    return (x-2)**2+2
"""
模拟梯度下降
"""
theta=-7.5  #表示梯度下降开始的点
dyv=0.0;  #表示当前最小theta的y
eta=0.1 #表示下降步长
arr=[] #记录所有下降的theta的点 方便绘图
while True:
    gradi=gradient(theta) #获取梯度
    dyv=dy(theta);  #获取当前点的y值
    arr.append(theta);
    if np.abs(gradi)<1e-8:
        break;
    theta = theta - eta * gradi;

print("最小y值的x点的坐标：",theta);
print("最小的y值：",dyv);
arr=np.array(arr);
plot.plot(arr,(arr-2)**2+2,"or",marker="*")
plot.show();

