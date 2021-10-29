#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : mpl_squares.py
# @Time    : 2021/10/29 17:51
# @Author  : Leo
# @Software: PyCharm
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()