import time
print(2**31-1) #This is the largest possible value for a signed 32 bit integer
print(time.ctime(2**31-1)) #Which corresponds to this as the deadline to switch
print(2**32-1) #This is the largest possible value for an unsigned 32 bit integer
print(time.ctime(2**32-1)) #Which corresponds to this as the deadline to switch
#However in python3 integers can be arbitrarily large regardless of the underlying system.
#So the issue could be circumvented by implementing a pure python time library that doesn't depend on the underlying operating system libraries affected by this issue

#smallest signed value with n bits is -2**(n-1)
mn=1
while 1+2**(-mn+1) !=1:
    mn+=1
mn=mn-1 #as we want the largest mn for which 1+2**(-mn+1) !=1 holds
print(mn) #number of bits the mantissa (including sign) is stored as


#with n bits in the exponent the smallest number you can represent is 2**(-2**(n-1))
pn=1
while 2**(-2**(pn-1))!=0:
    pn+=1
pn=pn-1 #as we want the largest pn for which 2**(-2**(pn-1))!=0 holds
print(pn) #number of bits the exponent (including sign) is stored as
