import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import Chapter2integrator


def erroranalysis(a,b,B,f=lambda x: np.exp(-x**2)):
    x=[]
    for n in range(B):
        x.append(abs(Chapter2integrator.fivepoint(a,b,f=f,B=n+1)-np.sqrt(np.pi)))
    return(x)

blocks=[i+1 for i in range(36)]
error2=erroranalysis(-2,2,10)
error3=erroranalysis(-3,3,10)
error4=erroranalysis(-4,4,20)
error5=erroranalysis(-5,5,25)
error6=erroranalysis(-6,6,35)
error7=erroranalysis(-7,7,35)

plt.plot(blocks[:10],error2, label='between -2 and 2')
plt.plot(blocks[:10],error3,label='between -3 and 3')
plt.plot(blocks[:10],error4[:10],label='between -4 and 4')
plt.plot(blocks[:10],error5[:10],label='between -5 and 5')
plt.legend()
plt.show()

# Here we see that using larger intervals greatly increases the error for low number of blocks. This is due to the block size being increased in those situations.

plt.plot(blocks[10:18],error4[10:18],label='between -4 and 4')
plt.plot(blocks[10:18],error5[10:18],label='between -5 and 5')
plt.legend()
plt.show()


plt.plot(blocks[17:22],error5[17:22],label='between -5 and 5')
plt.plot(blocks[17:22],error6[17:22],label='between -6 and 6')
plt.legend()
plt.show()

plt.plot(blocks[24:35],error6[24:35],label='between -6 and 6')
plt.plot(blocks[24:35],error7[24:35],label='between -7 and 7')
plt.legend()
plt.show()

# Across the last few plots we see how increasing the number of block lowers the error towards a "minimum" within each intervall.
#Increasing the size of the intervall lowers the "minimum" error but increases the number of block you need to reach it as the blocks become larger.
#In the last plot we see how we reach the max precision and no longer decrease the error by either increasing intervall size or number of blocks.