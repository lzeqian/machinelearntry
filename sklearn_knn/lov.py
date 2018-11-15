import numpy as np;
import matplotlib.pyplot as pl
import matplotlib.lines as mlines
"""
  读取data.txt的所有数据集
  前三列：
    海伦收集的样本数据主要包含以下3种特征：
        每年获得的飞行常客里程数
        玩视频游戏所消耗时间百分比
        每周消费的冰淇淋公升数
  最后一列：
    didntLike 不喜欢的人
    smallDoses 魅力一般的人
    largeDoses 极具魅力的人
  
"""
def dataSet():
    arr=[];
    with open("lovedata.txt","r") as file:
        for line in file:
            arr.append(line.replace("\n","").split("\t"));
    arrnp=np.array(arr);
    return arrnp[:,:3],arrnp[:,3:].T[0];

'''
绘制图形
'''
def graphDataSet():
    feature, result = dataSet()
    pl.rcParams['font.family'] = ['STFangsong']
    #nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域 figsize表示画布大小
    fig,axs=pl.subplots(nrows=2,ncols=2);# """,figsize=(13,8)"""
    axs[0][0].set_title("每年获得的飞行常客里程数和玩视频游戏所消耗时间百分比占比")
    axs[0][0].set_xlabel("每年获得的飞行常客里程数")
    axs[0][0].set_ylabel("玩视频游戏所消耗时间")
    colorArray=["black" if e=="didntLike"  else ("orange" if e=="smallDoses" else "red") for e in result]
    axs[0][0].scatter(x=feature[:,:1].T[0],y=feature[:,1:2].T[0],color=colorArray,s=2);
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                              markersize=2, label='不喜欢')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                               markersize=2, label='魅力一般')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                               markersize=2, label='极具魅力')
    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    #####绘制 0,1这个subplot 上面代码用于学习
    drawSubPlot(axs,0,1,"玩视频游戏所消耗时间和每周消费的冰淇淋公升数占比"
                ,"玩视频游戏所消耗时间",
                "每周消费的冰淇淋公升数",
                feature[:, 1:2].T[0],
                feature[:, 2:3].T[0],
                colorArray
                )
    drawSubPlot(axs, 1, 0, "每年获得的飞行常客里程数和每周消费的冰淇淋公升数占比"
                , "每年获得的飞行常客里程数",
                "每周消费的冰淇淋公升数",
                feature[:, 0:1].T[0],
                feature[:, 2:3].T[0],
                colorArray
                )
    pl.show();
"""
  0 0 0,1
  0 1 1,2
  1 1 0,2

"""
def drawSubPlot(axs,x,y,title,xlabel,ylabel,xdata,ydata,colorArray):
    axs[x][y].set_title(title)
    axs[x][y].set_xlabel(xlabel)
    axs[x][y].set_ylabel(ylabel)
    axs[x][y].scatter(x=xdata, y=ydata, color=colorArray, s=2);
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                              markersize=2, label='不喜欢')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                               markersize=2, label='魅力一般')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                               markersize=2, label='极具魅力')
    axs[x][y].legend(handles=[didntLike, smallDoses, largeDoses])

'''
  knn算法 算出离给定数据最近的点
'''
def knn(airplane,game,ice,k):
    print();
graphDataSet()