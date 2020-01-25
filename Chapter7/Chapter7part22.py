import math
import pylab
import matplotlib
matplotlib.use('Qt5Agg')
def expliciteulerLV(A,B,C,D,x0,y0,h,N):
    x=[x0]
    y=[y0]
    for n in range(1,N):
        x_n=x[n-1]+h*x[n-1]*(A-B*y[n-1])
        y_n=y[n-1]+h*y[n-1]*(C*x[n-1]-D)
        x.append(x_n)
        y.append(y_n)
    return([x,y])
def symplecticeulerLV(A,B,C,D,x0,y0,h,N):
    x = [x0]
    y = [y0]
    for n in range(1, N):
        x_n=x[n-1]+h*x[n-1]*(A-B*y[n-1])
        x.append(x_n)
        y_n=y[n-1]+h*y[n-1]*(C*x[n]-D)
        y.append(y_n)
    return ([x, y])


v1=expliciteulerLV(2/3,4/3,1,1,0.9,0.9,0.1,1000)
v2=symplecticeulerLV(2/3,4/3,1,1,0.9,0.9,0.1,1000)
pylab.plot(v1[0],v1[1])
pylab.show()
pylab.plot(v2[0],v2[1])
pylab.show()

#Here we see that the symplectic euler method produces the characteristic closed loop we expect from the loktera-volta equations.
#While the explicit euler method approximates it well initialy it blows up as t increase and becomes wildly inaccurate.
#Multiple small errors add up leading to the solution breaking its charecteristic physical properties
#This is due to the fact that the symplectic euler method preserves H due as can be seen below.

def findH(x,y,A,B,C,D):
    H=[0]*len(x)
    for i in range(len(x)):
        H[i]=C*x[i]+B*y[i]-math.log((x[i]**D)*(y[i]**A))
    return(H)
H1=findH(v1[0][:700],v1[1][:700],2/3,4/3,1,1)
H2=findH(v2[0],v2[1],2/3,4/3,1,1)
pylab.plot(H1)
pylab.show()
pylab.plot(H2)
pylab.show()


