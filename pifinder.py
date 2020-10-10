import matplotlib.pyplot as plt
import random as rd
#import math
import numpy as np
def app(n,size):
    """size: size for the dots
    n for number of dots more you add dots more you take aproximate to pi """
    numcir = 0
    numtotal = n
    xr = []
    yr = []
    e = []
    b = []
    for i in range(0,n):
        x = rd.uniform(-1,1)
        y = rd.uniform(-1,1)
        xr.append(x)
        yr.append(y)
        if (x**2 + y**2)<1:
            numcir +=1
            e.append(x)
            b.append(y)
    pi = 4*(numcir/numtotal)
    plt.axis('equal')
    plt.plot(xr,yr,'ko', markersize=size,color="blue")
    plt.axis('equal')
    plt.plot(e,b,' ko', markersize=size,color="red")
    plt.title("pi is " + str(pi)+" approximation is "+str(abs(np.pi-pi)))
    plt.show()
  
