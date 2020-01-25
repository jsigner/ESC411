import  Chapter2integrator
import Chapter2part8
import numpy as np

def Chebyshevsp(f,g,B=8):
    return (Chapter2integrator.fivepoint(-1, 1, f=lambda x: f.eval(x) * g.eval(x)/np.sqrt(1-x**2), B=B))

def Chebyshevnorm(f,B=8):
    return(np.sqrt(Chebyshevsp(f,f,B=B)))

def chebyshevgenerator(N,B=8):
    '''generate first N chebyshev polynomials using 5 point Newton-Coates integrator'''
    v=[Chapter2part8.Polynomial([0]*n+[1]) for n in range(N)]
    u=Chapter2part8.normalize(Chapter2part8.orthogonalization(v,Chapter2part8.projection,lambda f,g:Chebyshevsp(f,g,B=B)),lambda f:Chebyshevnorm(f,B=B))
    un=[u[n]*np.sqrt(np.pi/2) for n in range(N)]
    un[0]=u[0]*np.sqrt(np.pi)
    return(un)

print(chebyshevgenerator(5))

def Chebyshevsp2(f,g,M=1):
    return (Chapter2integrator.gausschebyshev(f=lambda x: f.eval(x)*g.eval(x), M=M))

def Chebyshevnorm2(f,M=1):
    return(np.sqrt(Chebyshevsp2(f,f,M=M)))

def chebyshevgenerator2(N,M=4):
    '''generate first N chebyshev polynomials using Gauss-Chebyshev quadrature'''
    v=[Chapter2part8.Polynomial([0]*n+[1]) for n in range(N)]
    u=Chapter2part8.normalize(Chapter2part8.orthogonalization(v,Chapter2part8.projection,lambda f,g:Chebyshevsp2(f,g,M=M)),lambda f:Chebyshevnorm2(f,M=M))
    un=[u[n]*np.sqrt(np.pi/2) for n in range(N)]
    un[0]=u[0]*np.sqrt(np.pi)
    return(un)

print(chebyshevgenerator2(6,M=6))

#The results for n>=M are nonsensical as in the orthoganilsation procedure we evaluate integrals of order 2n
#So if n>=M we use Gauss chebyshev-quadrature for polynomials of degree >=2M so the results do not make much sense