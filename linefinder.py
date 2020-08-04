# finding the line of best fit for a data set
from matplotlib import pyplot as plt
import random

def summer(x):
   sum = 0
   for value in x:
     sum+=int(value)
   return sum

def line(x,y):
  xsum=summer(x)
  ysum=summer(y)
  xpmean=xsum/len(x) #mean of xvalues
  ypmean=ysum/len(y) #mean of yvalues

  xbar = [] # x-meanx
  ybar = [] # y-meany
  xbar2 = [] # xbar ^2
  ybar2 = [] # ybar ^2
  xybar = []
  for i in range(len(x)):
    xbari = x[i]-xpmean
    ybari = y[i]-ypmean 
    xbar.append( xbari )
    ybar.append( ybari )

    xbar2.append( xbari**2 ) 
    ybar2.append( ybari**2 )

    xybar.append( xbari * ybari )
  
  xbar2sum = summer(xbar2)
  xybarsum = summer(xybar)

  m = xybarsum / xbar2sum

  c = ypmean - (m * xpmean)
  return [m,c] #grad, y-intercept
  
# ## Example for testing
# x= [1,2,3,4,5,6,7,8,9,10]
# y= [2,4,6,8,10,12,14,16,18,20]
# or
# y=[]
# for ye in range(10):
#   y.append(ye)

# plt.plot(x,y,'o')

# m,c = line(x,y)
# nx=[]
# ny=[]
# for xn in range(-5,20):
#  nx.append(xn)
#  ny.append((xn*m) + c)

# plt.plot(nx,ny)
# plt.show()