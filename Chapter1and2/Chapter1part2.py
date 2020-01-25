import functools
import math
import cmath
import numpy as n
import pylab
import matplotlib
matplotlib.use('Qt5Agg')

d=[2,4,8,16,32,64,128]
u=functools.reduce(lambda s, n : n+ 1/s,d[::-1])
print(u)
s=functools.reduce(lambda s, n : s + [s[-1]+ cmath.rect(1,(n**2)*math.pi/u)], range(10001), [0])
s=n.array(s)
pylab.plot(s.real,s.imag)
pylab.show() #The original curlicue from figure 1.1

d2=[2,4,8,16,32,64,128]
u2=functools.reduce(lambda s, n : n+ 1/s,d[::-1])-2
print(u2)
L2=int(10001//0.2)
s2=functools.reduce(lambda s, n : s + [s[-1]+ cmath.rect(1,(n**2)*math.pi/u2)], range(L2), [0])
s2=n.array(s2)
pylab.plot(s2.real,s2.imag)
pylab.show() #The scaled and reflected curlicue created by removing the first term and replacing L by L/mu
