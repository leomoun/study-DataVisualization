#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : cubes.py
# @Time    : 2021/11/1 15:24
# @Author  : Leo
# @Software: PyCharm
# 15-1, 15-2
import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# x_values = [1, 2, 3, 4, 5]
# y_values = [x**3 for x in x_values]
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=[[0, 0.3, 0]], s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.hsv, s=10)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("立方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0, 5100, 0, 5100**3])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
