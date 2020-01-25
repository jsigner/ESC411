from itertools import zip_longest
import numpy as np
import Chapter2integrator

class Polynomial(object):
    def __init__(self, coeff):
        self.coeff=coeff
    def __str__(self):
        s = ''
        X = ['']
        for i in range(1, len(self.coeff)):
            if self.coeff[i] > 0:
                s += '+' + str(self.coeff[i]) + 'X^' + str(i)
            if self.coeff[i] < 0:
                s += str(self.coeff[i]) + 'X^' + str(i)
        if self.coeff[0] != 0:
            s = str(self.coeff[0]) + s
        else:
            s = s[1:]
        if s == '':
            s = '0'
        return(s)

    def __add__(self,other):
        if isinstance(other,Polynomial):
            return(Polynomial([a+b for a,b in zip_longest(self.coeff,other.coeff,fillvalue=0)]))
        else:
            newcoeff=[self.coeff[0]+other]
            newcoeff.extend(self.coeff[1:])
            return(Polynomial(newcoeff))
    def __radd__(self,other):
        return(self.__add__(other))
    def __sub__(self,other):
        if isinstance(other, Polynomial):
            return(Polynomial([a-b for a,b in zip_longest(self.coeff,other.coeff,fillvalue=0)]))
        else:
            newcoeff=[self.coeff[0]-other]
            newcoeff.extend(self.coeff[1:])
            return(Polynomial(newcoeff))
    def __rsub__(self, other):
        return (self.__sub__(other))
    def __mul__(self, other):
        return(Polynomial([other*i for i in self.coeff]))
    def __rmul__(self, other):
        return(self.__mul__(other))
    def __truediv__(self, other):
            return(self.__mul__(1/other))
    def order(self):
        return(len(self.coeff)-1)
    def __repr__(self):
        return(str(self))
    def eval(self,x):
        sum = self.coeff[-1]
        n=self.order()
        for k in range(n, 0, -1):
            sum = x*sum+self.coeff[k-1]
        return sum

def orthogonalization(v,proj,sp):
    u=v
    for i in range(1,len(v)):
        u[i]=v[i]-sum([proj(v[i],u[j],sp) for j in range(i)])
    return(u)
def projection(v,u,sp):
    return(((sp(v,u)/sp(u,u))*u))
def L2sp(f,g,B=8):
    return(Chapter2integrator.fivepoint(-1,1,f=lambda x: f.eval(x)*g.eval(x),B=B))

v=[Polynomial([1]),Polynomial([0,1]),Polynomial([0,0,1]),Polynomial([0,0,0,1]),Polynomial([0,0,0,0,1])]
def normalize(v,norm):
    return([p/norm(p) for p in v ])

def L2norm(f,B=8):
    return(np.sqrt(L2sp(f,f,B=B)))


def legendregenerator(N,B=8):
    '''generate first N lagrange polynomials'''
    v=[Polynomial([0]*n+[1]) for n in range(N)]
    u=normalize(orthogonalization(v,projection,lambda f,g: L2sp(f,g,B=B)),lambda f: L2norm(f,B=B))
    return([u[n]/np.sqrt((n+(1/2))) for n in range(N)])

#print(legendregenerator(7))

#the first few are correct to roundoff as the integrals are exact for polynomial of degree less than five
#p0,p1,p2,p3 have no integrals of polynomials with order greater than five so are exact