import sys
import numpy as np
import math
from scipy.special import roots_legendre, eval_legendre
import matplotlib.pyplot as plt

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('inter_inputI.txt','r')
o = open('inter_outputI.txt','a')

tokenized = read_by_tokens(f)

fun = str(next(tokenized))

def func(x):
    return eval(fun)

a = float(next(tokenized))
b = float(next(tokenized))
err=float(next(tokenized))
ch= int(next(tokenized))

def Trapm(h,n):
    sum=func(a)
    i=1
    while(i<n):
        sum=sum+2*func(a+i*h/n)
        i=i+1
    sum=sum+func(b)
    return (h/n)*sum/2

def Romberg():
    I=np.zeros((10,10))
    n=1
    I[0][0]=Trapm(b-a,n)
    iter=0
    while True:
        iter=iter+1
        n=pow(2,iter)
        I[iter][0]=Trapm(b-a,n)
        for k in range(1,iter+1):
            I[iter][k]=(pow(4,k)*I[iter][k-1] - I[iter-1][k-1])/(pow(4,k)-1)
        ea= abs((I[iter][iter])-I[iter][iter-1])/(I[iter][iter])*100
        #print(iter)
        if ea<err:
            #print("here")
            break
    return (I[iter][iter],n,ea)

def GaussQ():
    n=1
    Gold=999999
    fu=np.vectorize(func)
    while True:
        [x,w] = roots_legendre(n)
        Gnew=0.5*(b-a)*sum(w*fu(0.5*(b-a)*x+0.5*(b+a)))
        if(abs((Gold-Gnew)/Gnew)*100 < err):
            return (Gnew,n,(Gold-Gnew)/Gnew*100)
        Gold=Gnew
        n=n+1

if ch==1:
    ans = Romberg()
    p = ans[1]
    o.write("\nROMBERG\nIntegral Value: " + str(ans[0]))
    o.write("\nNo. of Intervals: " + str(ans[1]))
    o.write("\nRelative Error: " + str(ans[2]))
    arrx=np.zeros(p+1)
    arry=np.zeros(p+1)
    for i in range(p+1):
        arrx[i]=a+(b-a)/p*i
        arry[i]=func(arrx[i])

    plt.plot(arrx, arry, color="blue")
    plt.fill_between(arrx, arry, color="pink", alpha=.23)
    plt.scatter(arrx, arry, color="red")
    plt.title("Romberg")

    plt.show()

if ch==2:
    ans=GaussQ()
    p = ans[1]
    o.write("\nGAUSS QUADRATURE\nIntegral Value: "+str(ans[0]))
    o.write("\nNo. of Gauss points: " + str(ans[1]))
    o.write("\nRelative Error: " + str(ans[2]))
    arrx = np.zeros(p + 2)
    arry = np.zeros(p + 2)
    arrx[0]=a
    arry[0]=func(a)
    x,w = roots_legendre(p)
    for i in range(p):
        arrx[i+1]=((b+a)+(b-a)*x[i])/2
        arry[i+1]=func(arrx[i+1])
    arrx[p+1]=b
    arry[p+1]=func(b)

    plt.plot(arrx, arry, color="blue")
    plt.fill_between(arrx, arry, color="pink",alpha=.23)
    plt.scatter(arrx, arry, color="red")
    plt.title("Gauss Quadrature")
    plt.show()





f.close()
o.close()
