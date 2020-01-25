import numpy as np
from functools import reduce

def fivepointsetup(a,b):  #Here I have solved the system by hand as some simple arithmetic operations are significantly faster than numpys solve function
    h = abs(b-a)/5
    x= [a+(i+0.5)*h for i in range(0, 5)]
    x1=x[3]
    x2=x[4]
    k=(3*b**2-5*x1**2)/(5*(x2**2-x1**2))
    c1=(b**3)*(1-k)/(3*x1**2)
    c2=(k*b**3)/(3*x2**2)
    return([x,[c2,c1,2*b-b**3*2*((1-k)/x1**2+k/x2**2)/3,c1,c2]])

def ppointintegrator(a,b,f=lambda x: np.exp(-x**2),p=5,pointsetup=fivepointsetup):
    '''p and pointsetup can be changed to easily change the number (or distribution) of points you integrate over'''
    midpoint=(a+b)/2
    setup=pointsetup(a/2-b/2,b/2-a/2)
    y=[f(x+midpoint) for x in setup[0]]
    coeff = setup[1]
    I=[y[i]*coeff[i] for i in range(0,p)]
    return(sum(I))




def fivepoint(a,b,f=lambda x: np.exp(-x**2),B=1):
    mesh=np.linspace(a,b,B+1) #here I have used linspace instead of a list as it is much faster for large b
    I=0
    for m in range(0,B):
        I+=ppointintegrator(mesh[m],mesh[m+1],f=f)

    return(I)

def gausschebyshev(f=lambda x:x*x,M=1):
    I=((np.pi/M)*reduce(lambda s, k:s+f((np.cos((k+1/2)*np.pi/M))),range(M),0))
    return(I)
