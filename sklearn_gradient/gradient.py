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

"""
  演示什么是梯度
  y=5-x 明显导数是 -1 -1表示往左侧增大 
  明显梯度下降就需要往右侧走 x-(-1)=x+1
  
"""
setXY()
darr=np.linspace(-10,10,10);
plot.plot(darr,5-darr);
plot.show();


"""
  演示什么是梯度
  y=5+x 明显导数是 1 1表示往右侧增大 
  明显梯度下降就需要往左侧走 x-(1)=x-1
  总结 梯度下降走的方向就是 x-(导数)
"""
setXY()
darr=np.linspace(-10,10,10);
plot.plot(darr,5+darr);
plot.show();

"""
  演示什么是梯度
  y=x**2+5 因为是一元二次方程 冥想不同的x点的梯度是不一样的
   y导数=2x x>0时 随着x的增大 梯度越大
          比如2.5 梯度是5
              5   梯度是10
"""
setXY()
darr=np.linspace(-10,10,10);
plot.plot(darr,darr**2+5);
plot.show();



