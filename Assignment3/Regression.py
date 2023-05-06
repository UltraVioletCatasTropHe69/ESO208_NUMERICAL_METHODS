import numpy as np
from numpy.polynomial import polynomial as P
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('inter_inputR.txt','r')

tokenized = read_by_tokens(f)

n = int(next(tokenized))

def polynomial(x,coeff,deg):
    sum=0
    for i in range(deg+1):
        sum=sum+coeff[i]*pow(x,i)
    return sum

x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    x[i]=float(next(tokenized))
    y[i]=float(next(tokenized))
#################################################################################
o = open('inter_outputR.txt', 'a')
plt.scatter(x, y, color='black', label='Data')
x_new = np.linspace(min(x), max(x), 10000)
count=1
color = iter(cm.rainbow(np.linspace(0, 1,4)))
while(count<5):
    deg = int(input("Enter the degree of the fitting polynomial: "))
    c, stats = P.polyfit(x, y, deg, full=True)
    o.write(str(deg)+"th degree coefficients: "+str(c)+"\n")
    corr_matrix = np.corrcoef(y,polynomial(x,c,deg))
    corr = corr_matrix[0, 1]
    R_sq = corr ** 2
    o.write("R Sq: "+str(R_sq)+"\n")
    y_new = polynomial(x_new,c,deg)
    stri="Polynomial of degree "+str(deg)
    c = next(color)
    plt.plot(x_new, y_new, color=c, label=stri)
    count=count+1
plt.grid(axis='y')
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.legend()
plt.show()
o.close()
f.close()
