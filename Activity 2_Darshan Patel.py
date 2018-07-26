# -*- coding: utf-8 -*-
"""
Programmer: Darshan Patel
Project: Python Session Activity 2
Date: July 23rd, 2018
Code Description: Analyze given data and plot the graphs
Company: KPIT
Copyright: KPIT C 2018
"""

import pandas as panda
import matplotlib.pyplot as plt
import math

file = panda.read_csv("C:/Users/darshanp5/Desktop/data.csv")

xacc = file['RL_xacc']          # X-axis acceleration data
yacc = file['RL_yacc']          # Y-axis acceleration data
zacc = file['RL_zacc']          # Z-axis acceleration data

rmsacc = list()

for i in range(124):
    rmsacc.append(math.sqrt(pow(xacc[i], 2)+pow(yacc[i], 2)+pow(zacc[i], 2)))

plt.plot(rmsacc)
plt.axhline(y=22.5, color='r')
plt.xlabel('Time')
plt.ylabel('RMS Acceleration')
plt.show

counter = 0

for i in rmsacc:
    if i >= 22.5:               # 22.5 is local minimum and a threshold
        counter += 1                # to count a peak as a step

print ('Steps: ', counter)
