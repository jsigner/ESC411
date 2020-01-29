import random
import math
import numpy
import pylab
import matplotlib
matplotlib.use('Qt5Agg')
def puppetwalk(M,D):
    MC=M
    DC=D
    S=M+D
    X=[0]
    Mstep=D/(M+D)
    Dstep=M/(M+D)
    for n in range(S):
        if random.randint(0,1):
            X.append(X[n]+Mstep)
            MC+=-1
        else:
            X.append(X[n]-Dstep)
            DC+=-1
        if MC==0:
            for n in range(DC):
                X.append(X[-1]-Dstep)
            break
        elif DC==0:
            for n in range(MC):
                X.append(X[-1]+Mstep)
            break
    return(X)

tests=10000
N1=24
N2=36
maxdifference=[]
for n in range(tests):
    maxdifference.append(abs(max(puppetwalk(N1,N2),key=abs))/((N1+N2)/2))

v=math.sqrt(N1*N2/(N1+N2))
u=v+0.12+0.11*v
S=numpy.linspace(0.02,0.5,100)
k=numpy.array(list(range(20)))
cdf=[1-2*sum(((-1)**k)*numpy.exp((-2*(k+1)**2)*(u**2)*(s**2))) for s in S]

pylab.hist(maxdifference,40,cumulative=True,density=True)
pylab.plot(S,cdf,'r')
pylab.show()

#There is a very good fit for fractional differences over 0.2 below that it undershoots a little

