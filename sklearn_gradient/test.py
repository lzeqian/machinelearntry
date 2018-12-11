import numpy as np;
import matplotlib.pyplot as plot
arr1=np.array([[1,2],[2,3]])
arr2=np.array([10,5])
print(arr1.dot(arr2))
#print(np.empty((3)))

a=np.array([4.42312853e-14,2.18902674e-14])
print(np.all(a <= 1e-5))
print(4.42312853e-14<=1e-5)
print(2.18902674e-14<=1e-5)