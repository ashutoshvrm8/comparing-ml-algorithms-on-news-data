import numpy as np
import matplotlib.pyplot as plt

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.07       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

xvals = [15, 22, 23,11]
rects1 = ax.bar(ind, xvals, width, color='r')
yvals = [4, 9, 2]
rects2 = ax.bar(ind, yvals, width, color='g')
zvals = [1,2,3]
rects3 = ax.bar(ind+width*2, zvals, width, color='b')
kvals = [11,12,13]
rects4 = ax.bar(ind+width*3, kvals, width, color='y')


ax.set_title('Performance Comparision Bar Chart')
ax.set_ylabel('Range')
ax.set_xlabel('Classifers')
ax.set_xticks(ind+width)
ax.set_xticklabels(('precision', 'recall', 'f1-score'))
ax.legend((rects1[0],rects2[0],rects3[0],rects4[0]),('SVM','Decision Tree', 'Random Forest', 'Extra Trees'),loc='lower right')

plt.axes().yaxis.grid() # for horizontal grids


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()