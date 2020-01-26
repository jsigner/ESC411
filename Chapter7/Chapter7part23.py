import numpy as np
def diff2(u):
    N = len(u)
    d2u = [0]*N
    d2u[0] = u[1]-u[0]
    d2u[N-1] = u[N-2]-u[N-1]
    for n in range(1,N-1):
        d2u[n] = u[n+1] + u[n-1]-2*u[n]
    return(np.array(d2u))

def RHS(u,dx):
    N=len(u)
    d2=diff2(u)
    r=np.array([0.0 for n in range(N)])
    for n in range(0,N):
        r[n]=u[n]*(1-u[n])+d2[n]/dx**2
    return(r)


def numsolFK(u0,dx,dt,N):
    n=len(u0)
    u=[np.array([0.0]*n) for i in range(N)]
    u[0]=u0
    for t in range(1,N):
        u[t]=u[t-1]+dt*RHS(u[t-1]+(dt/2)*RHS(u[t-1],dx),dx)
        #print(dt*RHS(u[t] + (dt / 2) * RHS(u[t], dx), dx))
    return(u)


print(numsolFK(np.array([0,0,0,2.5,1,0,0]),0.1,0.1,100))
