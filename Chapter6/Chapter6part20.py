import math
import random
import numpy as np
import pylab
import matplotlib
matplotlib.use('Qt5Agg')
a=-0.5
b=0.7
N=100
M=10000
phimin=math.atan((-1-a)/b)
phimax=math.atan((1-a)/b)

x=[]
for i in range(N):
    x.append(a+b*math.tan(random.uniform(phimin,phimax)))
x=np.array(x)

#pylab.hist(x,20,density='1')
#pylab.show()

A=[0]
B=[0.5]
for m in range(M):
    ap=A[m]+random.normalvariate(0,1) #any symetric distribution
    bp=B[m]+random.normalvariate(0,1) #any symetric distribution
    A.append(A[m])
    B.append(B[m])
    if -1<=ap<=1 and bp>=0: #checks that P(ap,bp)=/=0 as then the step is rejected anyway
        test=np.prod(((-math.atan((A[m]-1)/B[m])+math.atan((A[m]+1)/B[m]))*bp*(B[m]**2+(x-A[m])**2)/((-math.atan((ap-1)/bp)+math.atan((ap+1)/bp))*B[m]*(bp**2+(x-ap)**2))))
        if random.uniform(0,1)<=test:
            A[m+1]=ap
            B[m+1]=bp


pylab.hist(A,20)
pylab.show()

pylab.hist(B,20)
pylab.show()




