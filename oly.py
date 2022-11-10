# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:47:43 2022

@author: cse8
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/cse8/Desktop/ol/athlete_events.csv')
#print(data)
df=pd.DataFrame(data)
#plt.hist(data['Age'])
#print(df[data['Year']==2000]['Medal'].value_counts().plot(kind='bar'))
#print(df[data['Sex']=='M']['Medal'].value_counts().plot(kind='bar'))
#plt.scatter(x='height',y='weight',data=data)
#print(data['Height'],data['Weight'].value_counts().plot(kind='scatter'))
plt.scatter(data['Height'],data['Weight'])
