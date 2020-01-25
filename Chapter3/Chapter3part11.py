def gcd(a,b):
    if b == 0:
        return(a)
    q=a//b
    return gcd(b,a-q*b)
def findprimes(n):
    m=n+1
    p=[]
    nl=[0,0]+[1]*(n-1)
    for q in range(m):
        if nl[q]:
            p.append(q)
            for l in [(i+2)*q for i in range(n//q-1)]:
                nl[l]=0
    return([p,nl])
def checkcriterion(q):
    for a in range(1,q):
        if gcd(a,q)==1:
            if pow(a,q-1,q)!=1:
                return(False)
    return(True)

def findcarmeichelnumbers(n):
    cn=[]
    l=findprimes(n+4)[1]
    for i in range(1,1+n//2):
        a=2*i+1
        if not l[a]:         #as carmeichel number must be odd
            if checkcriterion(a):
                cn.append(a)
    return(cn)

            
