from functools import reduce
import math
import gcd
def bernoulinumbersfast(n):
    B=[1,-1/2]
    while len(B)<n:
        k=len(B)
        c=[(math.factorial(k)/(math.factorial(m)*math.factorial(k-m+1)))*B[m] for m in range(k)]
        B.append(-reduce(lambda s,n:n+s,c,0))
    return(B)

def factorial(n): #obviously significantly slower than math.factorial
    if not n:
        return(1)
    return(reduce(lambda s, n : n*s,range(1,n+1)))

def bernoulinumbersfractions(n):
    B=[[1,1],[-1,2]]
    while len(B)<n:
        k=len(B)
        c=[[-factorial(k)*B[m][0],(factorial(m)*factorial(k-m+1))*B[m][1]] for m in range(k)]
        B.extend(gcd.addfractions(c))
    return(B)
def bernoulinumbersslow(n):
    return([b[0]/b[1] for b in bernoulinumbersfractions(n)])

print(bernoulinumbersfast(10))
print(bernoulinumbersfractions(10))
print(bernoulinumbersslow(10))