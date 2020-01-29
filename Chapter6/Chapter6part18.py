import random
import math
import pylab
import matplotlib
import numpy
matplotlib.use('Qt5Agg')

def steptype1(mind,maxd):
    theta=random.uniform(0,2*math.pi)
    d=random.uniform(mind,maxd)
    return([d*math.cos(theta),d*math.sin(theta)])

def randomwalk(N):
    x=[0]*N
    y=[0]*N
    for n in range(1,N):
        step=steptype1(1,2)
        x[n]=x[n-1]+step[0]
        y[n]=y[n-1]+step[1]
    return([x,y])

def randomwalkendpoints(N):
    x=0
    y=0
    for n in range(1,N+1):
        step=steptype1(0,2)
        x=x+step[0]
        y=y+step[1]
    return([x,y])

def endpointlist(walk,N,M):
    x=[]
    y=[]
    for i in range(M):
        endpoint=walk(N)
        x.append(endpoint[0])
        y.append(endpoint[1])
    return([x,y])
N=50
M=10000
endpoints=endpointlist(randomwalkendpoints,N,M)

t1=numpy.linspace(-25,25,100)
normal=(1/(math.sqrt(N*math.sqrt(2)*math.pi)))*numpy.exp(-(1/(math.sqrt(2)*N))*(t1)**2)
pylab.hist(endpoints[0],40,density='1')
pylab.plot(t1,normal,'r')
pylab.show()

t2=numpy.linspace(-25,25,100)
normal=(1/(math.sqrt(N*math.sqrt(2)*math.pi)))*numpy.exp(-(1/(math.sqrt(2)*N))*(t1)**2)
pylab.hist(endpoints[1],40,density='1')
pylab.plot(t1,normal,'r')
pylab.show()



def distance(l):
    d=[]
    for i in range(len(l[0])):
        d.append(math.sqrt((l[0][i])**2+(l[1][i])**2))
    return(d)
finaldistance=distance(endpoints)
t3=numpy.linspace(0,25,100)
maxwelian=(2*t3/(N*math.sqrt(2)))*numpy.exp(-(1/(math.sqrt(2)*N))*(t3)**2)
pylab.hist(finaldistance,40,density='1')
pylab.plot(t3,maxwelian,'r')
pylab.show()