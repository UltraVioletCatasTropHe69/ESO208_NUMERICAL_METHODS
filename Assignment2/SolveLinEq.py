import numpy as np
from numpy.linalg import *

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('input.txt','r')
tokenized = read_by_tokens(f)

n = int(next(tokenized))

a = np.empty((n,n))
#print("\nMatrix a : \n", a)

for i in range (0,n):
        for j in range(0, n):
            a[i][j] = float(next(tokenized))
            # loops over all tokens *except the first two*
            #print(float(token))
max_it = int(next(tokenized))
er = float(next(tokenized))
nrst = float(next(tokenized))
print(a)

def normalize(x):
    fac = abs(x).max()
    x_n = x / abs(fac)
    return fac, x_n

def power():
    o.write('\nPOWER METHOD\n')
    print(a)
    x = np.zeros([n],dtype=float)
    x[0]=1
    lambda_1 = 1
    o = open('output.txt', 'a')
    o.write("Iteration No.\tEigenvalue\n")

    for i in range(max_it):
        #er=np.dot(a,x)
        err=lambda_1
        x = np.dot(a, x)
        lambda_1, x = normalize(x)
        err=abs(lambda_1-err)/lambda_1*100
        o.write(str(i+1)+'\t\t\t\t'+str(lambda_1)+'\n')
        if err<er :
            break

    o.write('Eigenvalue:' + str(lambda_1))
    o.write('\nEigenvector:' + str(x) )
    o.close()

def QR():


    ab = a
    o=open('output.txt','a')
    o.write('\nQR METHOD\n')
    ev = np.zeros(n)
    err=100

    for i in range(max_it):

         q, r = qr(ab)
         ab = np.dot(r, q)
         temp=np.max(ev)
         for jj in range(0,n):
             ev[jj]=ab[jj][jj]
         temp2=np.max(ev)
         err=float(abs((temp2-temp)/temp2))*100
    #    #if i + 1 in p:
         o.write(f'Iteration {i + 1}:\n')
         o.write(str(ev))
         if(err<er):
             break
    o.close()


def inversePower():
    print(a)
    ab = inv(a)

    x = np.zeros([n], dtype=float)
    for i in range(0,n):
        x[i]=1
    lambda_1 = 1
    o = open('output.txt', 'a')
    o.write('\nINVERSE POWER\n')
    o.write("Iteration No.\tEigenvalue\n")

    for i in range(max_it):
        # er=np.dot(a,x)
        err = lambda_1
        x = np.dot(ab, x)
        lambda_1, x = normalize(x)
        err = abs(lambda_1 - err) / lambda_1 * 100
        o.write(str(i + 1) + '\t\t\t\t' + str(1/lambda_1) + '\n')
        if err < er:
            break

    o.write('Eigenvalue:' + str(1/lambda_1))
    o.write('\nEigenvector:' + str(x))
    o.close()

def inversePowerWithShift():
    print(a)
    d=a
    for i in range(0,n):
        d[i][i]=a[i][i]-nrst
    ab = inv(d)

    x = np.zeros([n], dtype=float)
    for i in range(0,n):
        x[i]=1
    lambda_1 = 1
    o = open('output.txt', 'a')
    o.write("Iteration No.\tEigenvalue\n")

    for i in range(max_it):
        # er=np.dot(a,x)
        err = lambda_1
        x = np.dot(ab, x)
        lambda_1, x = normalize(x)
        err = abs(lambda_1 - err) / lambda_1 * 100
        o.write(str(i + 1) + '\t\t\t\t' + str(1/lambda_1 + nrst) + '\n')
        if err < er:
            break

    o.write('Eigenvalue:' + str(1/lambda_1 + nrst))
    o.write('\nEigenvector:' + str(x))
    o.close()

ch = int(input("1.Power 2.Inverse Power 3.Inverse Power with shift 4.QR"))
if(ch==3):
    inversePowerWithShift()
if(ch==4):
    QR()
if(ch==1):
    power()
if(ch==2):
    inversePower()
