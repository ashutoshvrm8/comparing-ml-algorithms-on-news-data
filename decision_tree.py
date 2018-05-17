import numpy as np
from sklearn.svm import SVC
from sklearn import ensemble
from sklearn.cross_validation import train_test_split
from sklearn import neighbors
from sklearn import tree
import random as rm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
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
for i in range(0,len(f)):
    x=[]
    y=[]
    f1=open(f[i],'r')
    data=f1.readlines()
    for j in data:
        x.append(j)
        y.append(c)
    xt,xtt,yt,ytt=train_test_split(x,y,test_size=0.20)
    for j in range(0,len(xt)):
        Q.append((xt[j],yt[j]))
    for j in range(0,len(xtt)):
        Q1.append((xtt[j],ytt[j]))
    c+=1
rm.shuffle(Q)
Q=Q[:6000]
for i in  range(0,len(Q1)):
    Q.append(Q1[i])
for i in range(0,len(Q)):
    x_train.append(Q[i][0])
    y_train.append(Q[i][1])

vec = CountVectorizer()
vec.fit_transform(x_train)
sm = vec.transform(x_train)
sm1=sm.todense()
sm2=sm1[:len(x_train)-len(Q1)]
sm3=sm1[len(x_train)-len(Q1):]
y1_train=y_train[:-len(Q1)]
y1_train=np.array(y1_train)
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


