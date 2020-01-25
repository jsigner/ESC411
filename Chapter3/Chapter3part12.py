def word(n):
    str = ""
    while n > 0 :
        c = chr(n % 32 + 96)
        if c < "a" or c > "z" :
            c = " "
        str += c
        n //= 32
    return str

def evesfunction(cyphertext,N):
    r=1
    while True:
        if pow(cyphertext,r,N)==1:
            return(r)
        r+=1

def extended_gcd(a,b):
    s=[1,0]
    t=[0,1]
    r=[a,b]
    while r[1]!=0:
        q=r[0]//r[1]
        s=[s[1],s[0]-q*s[1]]
        t = [t[1],t[0] - q *t[1]]
        r = [r[1], r[0] - q *r[1]]
    return((s[0],t[0]))

#print(evesfunction(100156265,1024384027))     #this is commented out as it takes a really long time on my laptop. Maybe there is a smarter less brute force way of doing it



#this gives us r=256080004
#we now search for d' such that cd'=1+mr
#we hav assumed that c and r are coprime so this is in the form of the nizouet identity and we can use the extended gcd to find d'

print(extended_gcd(910510237,256080004))

#so d' is 32005

print(100156265**32005 %1024384027)

#so a is 45271717

print(word(45271717))