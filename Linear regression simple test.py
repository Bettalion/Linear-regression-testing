from matplotlib import pyplot as plt
import random
from linefinder import *
#linear regresion
# data=[]

def sortxy(data):
  x=[]
  y=[]
  for dataset in data:
    x.append(dataset[0])
    y.append(dataset[1])
  return [x,y]

def PlotD(data,m,c):
  x,y=sortxy(data)
  plt.plot(x,y,'o') # plain data (scatter)
  
  ny=[]
  for element in x:
    ny.append((int(m)*element) + int(c))
  plt.plot(x,ny) # line of 'best fit'
  
  plt.show()

def FindFit(data):
  x,y=sortxy(data)
  m,c = line(x,y)
  return [m,c] # gradient,intercept

def populate(ranger,data=[]):
 for x in range(ranger[0],ranger[1]):
 #equation: y=x^2
  y=x*-2+1                                            ###################################
  # y+=random.randint(-2,2) # make it more random
  data.append([x,y])
 return data


ranger = [0,10] #range (start,end)                  ###############################
data=populate(ranger)

# or comment lines 40,41 and have a custom data set in the form:
# data = [[x1,y1], [x2,y2]...]

m,c=FindFit(data)
sm = str(m)[:4]
sc = str(c)[:4] 
print(f'The approximate best fit line is y = {sm}x + {sc}')
try:
  f = open('Data.txt','a'
except:
  f = open('Data.txt','w')
f.write(f'For Data:\n (X,Y) = {data}\nThe approximate best fit line is y = {sm}x + {sc}\nWhere m === {m} & c === {c}\n||\n')
f.close()
PlotD(data,m,c)

#### the ranger and equation (indicated with line of hashes) can be coustomized