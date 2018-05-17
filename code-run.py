# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 01:22:48 2017

@author: verma
"""

import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn import ensemble
import random as rm
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

x=[]
y=[]
Q=[]
x_train=[]
y_train=[]
count=0
c=0
c1=0
c2=0
Q1=[]
neg=[]
pos=[]
xnew_train=[]
xnew_test=[]
ynew_train=[]
ynew_test=[]
y_model=[]
y1_model=[]
new_neg=[]
new_pos=[]
c=0
f=['e_acid.txt','e_murder.txt','e_cyber.txt','e_terrorist.txt','e_rape.txt','e_dowry.txt','e_theft.txt','e_domestic.txt','e_education.txt','e_social.txt','e_awards.txt','e_science.txt','e_medical.txt']
#f=['AcidData.txt','Charity.txt','CyberCrime.txt','DowryData.txt','EducationNews.txt','Murder_News.txt','NewAwardsNews.txt','NewNobelPrize.txt','NewScienceNews.txt','NewSmugglingNews.txt','SocialService.txt']
for i in range(0,len(f)):
    x=[]
    y=[]
    f1=open(f[i],'r')
    data=f1.readlines()
    for j in data:
        x.append(j)
        y.append(c)
    xt,xtt,yt,ytt=train_test_split(x,y,test_size=0.40)
    for j in range(0,len(xt)):
        Q.append((xt[j],yt[j])) 
    for j in range(0,len(xtt)):
        Q1.append((xtt[j],ytt[j])) #test
    c+=1
rm.shuffle(Q)

for i in  range(0,len(Q1)):
    Q.append(Q1[i])
for i in range(0,len(Q)):
    x_train.append(Q[i][0])
    y_train.append(Q[i][1])

vec = CountVectorizer()
vec.fit_transform(x_train)
sm = vec.transform(x_train)
sm2=sm[:len(x_train)-len(Q1)]
sm3=sm[len(x_train)-len(Q1):]
y1_train=y_train[:-len(Q1)]
y1_train=np.array(y1_train)

#------------------------------------

from sklearn import svm

acc=0
d=svm.SVC(kernel='linear', gamma=1)
d.fit(sm2,y1_train)
l1=d.predict(sm3)
for i in range(0,len(l1)):
    if l1[i]==Q1[i][1]:
        acc+=1
a=[]
for i in range(0,len(Q1)):
    a.append(Q1[i][1])
a=np.array(a)
print 'acc'
print acc
met=metrics.classification_report(a,l1)
print met

vals=[]
vals=met.split()
xvals=[vals[len(vals)-4], vals[len(vals)-3], vals[len(vals)-2]]

#------------------------------------

print '2\n'
acc=0
d=tree.DecisionTreeClassifier()
d.fit(sm2,y1_train)
l1=d.predict(sm3)
for i in range(0,len(l1)):
    if l1[i]==Q1[i][1]:
        acc+=1
a=[]
for i in range(0,len(Q1)):
    a.append(Q1[i][1])
a=np.array(a)
print 'acc'
print acc
met=metrics.classification_report(a,l1)
print met

vals=[]
vals=met.split()
yvals=[vals[len(vals)-4], vals[len(vals)-3], vals[len(vals)-2]]


#---------------------------------------



print '3\n'
acc=0
d=ensemble.RandomForestClassifier()
d.fit(sm2,y1_train)
l1=d.predict(sm3)
for i in range(0,len(l1)):
    if l1[i]==Q1[i][1]:
        acc+=1
a=[]
for i in range(0,len(Q1)):
    a.append(Q1[i][1])
a=np.array(a)
print 'acc'
print acc
met=metrics.classification_report(a,l1)
print met

vals=[]
vals=met.split()
zvals=[vals[len(vals)-4], vals[len(vals)-3], vals[len(vals)-2]]

#---------------------------------------



print '4\n'
acc=0
d=ensemble.ExtraTreesClassifier()
d.fit(sm2,y1_train)
l1=d.predict(sm3)
for i in range(0,len(l1)):
    if l1[i]==Q1[i][1]:
        acc+=1
a=[]
for i in range(0,len(Q1)):
    a.append(Q1[i][1])
a=np.array(a)
print 'acc'
print acc
met=metrics.classification_report(a,l1)
print met

vals=[]
vals=met.split()
kvals=[vals[len(vals)-4], vals[len(vals)-3], vals[len(vals)-2]]

#---------------------------------------

#----------- P L O T --------------


N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.07       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

rects1 = ax.bar(ind, xvals, width, color='r')
rects2 = ax.bar(ind+width, yvals, width, color='g')
rects3 = ax.bar(ind+width*2, zvals, width, color='b')
rects4 = ax.bar(ind+width*3, kvals, width, color='y')



ax.set_title('Performance Comparision Bar Chart')
ax.set_ylabel('Range')
ax.set_xlabel('Classifers')
ax.set_xticks(ind+width)
ax.set_xticklabels(('precision', 'recall', 'f1-score'))
ax.legend((rects1[0],rects2[0],rects3[0],rects4[0]),('SVM','Decision Tree', 'Random Forest', 'Extra Trees'),loc='lower right')

plt.axes().yaxis.grid() # for horizontal grids

plt.ylim((0.45,0.70))

plt.show()