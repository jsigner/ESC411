def nroot(x,n=2):
    y=x
    while True:
        y_temp=y+(x-y**n)/(n*y**(n-1))

        if y==y_temp:
            break
        y = y_temp
    return(y)

p=3
a=nroot(81,n=3)

print([a,a**p])

p2=2
#a2=nroot(8) #intrestingly doesnt seem to work for any 2^n with n odd 3^n ect works

#print([a2,a2**p2])
