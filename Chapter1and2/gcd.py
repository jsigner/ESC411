import sys
from functools import reduce
sys.setrecursionlimit(10000)
def gcd(a,b):
    if b == 0:
        return(a)
    q=a//b
    return gcd(b,a-q*b)
def simplify(f):
    g=gcd(f[0],f[1])
    return([f[0]//g,f[1]//g])
def addfractions(f):
    if len(f)==1:
        return(f)
    else:
        f[1]=simplify([f[0][0]*f[1][1]+f[1][0]*f[0][1],f[0][1]*f[1][1]])
        del f[0]
        return(addfractions(f))

def add2fractions(a,b):
    return(simplify([a[0]*b[1]+a[1]*b[0],a[1]*b[1]]))

def addfractions2(f):
    '''This code looks nicer however is also significantly slower'''
    return(reduce(add2fractions,f))

