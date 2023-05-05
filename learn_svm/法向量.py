import numpy as np
import matplotlib.pyplot as plot

from commons.common import setXY

setXY()
x=np.random.uniform(-1,1,100)
a=3
y=a*x;
y1=a*x+5;
plot.plot(x,y)
plot.plot(x,y1)
plot.plot([0,a],[0,-1])
plot.axis('equal')
plot.show()
