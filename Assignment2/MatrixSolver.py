import numpy as np
from numpy.linalg import *
import sys
import math

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('input1.txt','r')

tokenized = read_by_tokens(f)

n = int(next(tokenized))

a = np.zeros((n, n + 1))
mat = np.zeros((n,n))
b = np.zeros(n)


#print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(next(tokenized))
        if j<n:
            mat[i][j]=a[i][j]
        else:
            b[i]=a[i][n]



def fos(lowertri, b):
    n = lowertri.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / lowertri[0][0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(lowertri[i, :i], y[:i])) / lowertri[i, i]
    return y

def bas(uppertri, y):
    n = uppertri.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / uppertri[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(uppertri[i, i:], x[i:])) / uppertri[i, i]
    return x


def gausselimination():
    o = open('output1.txt', 'a')
    #n = int(input('Enter number of unknowns: '))
    o.write('\nGAUSS ELIMINATION WITHOUT PIVOTING\n')
    x = np.zeros(n)

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]  # back substitution

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    o.write('\n x: ')
    o.write(str(x))

def gaussPivoting():
    o = open('output1.txt', 'a')

    o.write('\nGAUSS WITH PIVOTING\n')
    M = a

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k + 1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n + 1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n - 1] = float(M[n - 1][n]) / M[n - 1][n - 1]
    for i in range(n - 1, -1, -1):
        z = 0
        for j in range(i + 1, n):
            z = z + float(M[i][j]) * x[j]
        x[i] = float(M[i][n] - z) / M[i][i]

    o.write('\nx: ')
    o.write(str(x))

# LU decomposition
def crout():
    o = open('output1.txt', 'a')
    o.write('\nCROUT\n')
    A=mat
    n = len(A)
    L = np.zeros((n,n),dtype=float)
    U = np.zeros((n, n), dtype=float)
    for j in range(n):
        U[j][j] = 1             # set the j,j-th entry of U to 1
        for i in range(j, n):  # starting at L[j][j], solve j-th column of L
            alpha = float(A[i][j])
            for k in range(j):
                alpha -= L[i][k]*U[k][j]
            L[i][j] = alpha
        for i in range(j+1, n):# starting at U[j][j+1], solve j-th row of U
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= L[j][k]*U[k][i]
            U[j][i] = tempU/L[j][j]

    y = fos(L, b)
    x = bas(U, y)
    o.write("\nx: ")
    o.write(str(x))
    o.write("\nLower Triangular\n")

    o.write("\nLower Triangular\n")

    # Displaying the result :
    o.write(str(np.array(L)))

    o.write("\nUpper Triangular\n")
    o.write(str(np.array(U)))

   # print(L.dot(U))

def doolittle():
    o = open('output1.txt', 'a')
    o.write('\nDOOLITTLE\n')
    #print(mat)

    m=mat
    L = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)


    factor=0
    for k in range(0,n-1):
        for i in range(k+1,n):
            print(m[k][k])
            factor = m[i][k]/m[k][k]
            m[i][k]=factor
            for j in range(k+1,n):
                m[i][j]=m[i][j]-factor*m[k][j]


    for i in range(0,n):
        for j in range(0,n):
            if j<i:
                L[i][j]=m[i][j]

            else:
                U[i][j]=m[i][j]
                L[i][i]=1
    # setw is for displaying nicely
    y=fos(L,b)
    x=bas(U,y)
    o.write("\nx: ")
    o.write(str(x))
    o.write("\nLower Triangular\n")

    # Displaying the result :
    o.write(str(L))
    o.write("\nUpper Triangular\n")
    o.write(str(U))
    #print(L.dot(U))


def cholesky():
    o = open('output1.txt', 'a')
    o.write('\nCHOLESKY\n')
    matrix=mat
    lmat = [[0 for x in range(n)]
            for y in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum1 = 0

            if j == i:
                for k in range(j):
                    sum1 = sum1 + pow(lmat[j][k], 2)
                lmat[j][j] = int(math.sqrt(matrix[j][j] - sum1))
            else:

                for k in range(j):
                    sum1 = sum1 + (lmat[i][k] * lmat[j][k])
                if lmat[j][j] > 0:
                    lmat[i][j] = int((matrix[i][j] - sum1) /
                                     lmat[j][j])


    #o.write('\CHOLESKY')
    # Displaying the result :
    lm = np.array(lmat)
    lm = np.linalg.cholesky(matrix)

    y = fos(lm, b)
    x = bas(lm.transpose(), y)
    o.write("\nx: ")
    o.write(str(x))
    o.write("\nLower Triangular\n")
    o.write(str(lm))

    o.write("\nUpper Triangular\n")
    o.write(str(lm.transpose()))



while(True):
    ch = int(input("1.Gauss without pivoting\n2.Gauss with pivoting\n3.Crout\n4.Doolittle\n5.Cholesky\n6.Exit"))
    if(ch==1):
        gausselimination()
    if(ch==4):
        doolittle()
    if(ch==2):
        gaussPivoting()
    if(ch==3):
        crout()
    if(ch==5):
        cholesky()
    if(ch==6):
        break
print("Done")