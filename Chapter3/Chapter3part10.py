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

l=findprimes(12)[1]
for i in range(1,len(l)):
    if l[i]:
        print(i)