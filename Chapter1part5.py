from functools import reduce
import sys
sys.setrecursionlimit(10000)
import gcd
def arctanintegerarithmetic(x,n):
    p=[ i for i in range(n+1) if i%2==1 ]
    numerator=0
    m=1
    while m<=n/2:
        numerator+=(((-1)**(m+1))*x**(n-p[m-1]))*reduce(lambda s, k:k*s,p[:m-1]+p[m:],1)
        m+=1
    denominator=(x**n)*reduce(lambda s, k:k*s,p,1)
    return([numerator,denominator])
order=120
[numt,dent]=arctanintegerarithmetic(5,order)
[num1,den1]=gcd.simplify([4*numt,dent])
[num2,den2]=gcd.simplify(arctanintegerarithmetic(239,order))
[num,den]=gcd.simplify([4*(num1*den2-num2*den1),den1*den2])
print([num,den])
d=50
print((num*10**d)//den) #set d to the number of accurate digits