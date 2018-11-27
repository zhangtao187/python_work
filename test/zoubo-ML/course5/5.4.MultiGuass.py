#!/usr/bin/python
#  -*- coding:utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


if __name__ == '__main__':
    x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]   #51j代表51个数
    #print(x1,x2,np.stack((x1,x2),axis=0))

    x = np.stack((x1, x2), axis=2)   #堆叠函数  axis=0代表  一堆与一堆之间添加，axis=1代表一列与一列之间堆叠，axis=2代表元素与元素之间堆叠

    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=(9, 8), facecolor='w')
    sigma = (np.identity(2), np.diag((3,3)), np.diag((2,5)), np.array(((2,1), (1,5))))
    for i in np.arange(4):
        ax = plt.subplot(2, 2, i+1, projection='3d')
        norm = stats.multivariate_normal((0, 0), sigma[i])
        y = norm.pdf(x)   #概率密度函数
        ax.plot_surface(x1, x2, y, cmap=cm.Accent, rstride=2, cstride=2, alpha=0.9, lw=0.3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.suptitle('二元高斯分布方差比较', fontsize=18)
    plt.tight_layout(1.5)
    plt.show()


