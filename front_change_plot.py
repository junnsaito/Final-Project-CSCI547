# -*- coding: utf-8 --
"""
Created on Sat Nov 21 21:28:35 2020

@author: jsait
"""
""""
The code for the calving front change during 1986-2009
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# A=np.arange(16).reshape(4, 4)
# B=pd.DataFrame(np.arange(16).reshape(4, 4))

feature=['2009', '2001', '1996','1986']
name=['auto', 'manual','error','retreat']
data=np.array([[4128133, 14357452, 19928504,41832362], [4044962, 14258901, 19846973,41950461],
                   [0.030, 0.0356, 0.014,0.042],[0,-7.95,-9.97,-13.67]])


df = pd.DataFrame(data, 
                  index=name,columns=feature)
import datetime

time_09=datetime.date(2009, 8, 3)
time_01=datetime.date(2001, 9, 15)
time_96=datetime.date(1996, 9, 2)
time_86=datetime.date(1986, 7,28)

t_list=[time_86,time_96,time_01,time_09]
df.to_csv('front_change.csv')
retreat=df.loc["retreat"] #retreat=df.iloc[3] same code
error=df.loc['error']

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.plot(t_list, retreat,'-or')
ax.fill_between(t_list, retreat+error, retreat-error,color='r', alpha=0.1)
plt.ylim([-15, 1])
ax.set_ylabel('Cumulative glacier front variations (km)',fontsize=10)
ax.set_xlabel('Time',fontsize=10)
fig.savefig('plot.png')
