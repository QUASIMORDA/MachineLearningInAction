from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels = kNN.file2matrix('data/kNN/datingTestSet2.txt')
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2,100000,-2,25])
#plt.xlabel('Percentage of Time Spent Playing Video Games')
#plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.xlabel('Frequent Flyer Miles Earned Per Year')
plt.ylabel('Percentage of Time Spent Playing Video Games')


plt.show()
