#coding=utf-8

import numpy as np

x=0.5
learning_rate=0.5
temp=[]
for i in range(1000):
    x+=learning_rate*np.sin(x)
    temp.append(x)
import matplotlib.pyplot as plt
import math
a=np.linspace(0,math.pi,1000)
plt.plot(a,np.sin(a))
plt.plot(temp,np.sin(temp))
plt.show()