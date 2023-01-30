import matplotlib.pyplot as plot
def setXY(axeSrc=None):
    # 获取当前坐标轴对象
    ax = plot.gca() if not axeSrc else axeSrc;

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