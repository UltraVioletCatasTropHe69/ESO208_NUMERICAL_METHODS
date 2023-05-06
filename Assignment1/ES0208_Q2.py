import numpy as np
import matplotlib.pyplot as plt
import math

expr = ""
def xaxis(inp):
    return 0


def func(inp):
    x=inp
    return eval(expr)


def quad_fact(r,s):
    discri = r**2 + 4*s
    if discri >0:
        real1=(r+ math.sqrt(discri))/2
        real2=(r- math.sqrt(discri))/2
        print("Roots :","%.4f"%real1," and ","%.4f"%real2)
    else:
        real1=r/2
        real2=r/2
        img1=math.sqrt(abs(discri))/2
        img2=-img1
        print("Roots: ", "%.4f" %real1, " + i","%.4f" %img1," and ","%.4f" % real2," + i","%.4f" % img2)


def curveplot():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel("x")
    plt.ylabel("f(x)")
    y = np.linspace(-40, 40, 1000)
    f2 = np.vectorize(func)
    f3 = np.vectorize(xaxis)
    z=f2(y)
    plt.plot(y,z, color="black")
    plt.plot(y, f3(y), color="red")
    plt.show()


def Bairstow():
    coeff=[]
    b = []
    c = []
    deg=int(input("Input the degree of polynomial: "))
    i=0
    while(i<=deg):
        print("Input coeff at a[",i,"]: ")
        coeff.append((float(input(" "))))
        b.append(0.0)
        c.append(0.0)

        i=i+1
    a=coeff
    error=float(input("Max relative percentage error: "))
    N=int(input("Max number of iterations: "))
    n=deg

    i=1
    global expr
    while(i<=deg):
        expr = expr +"+"+str(coeff[i])+"*x**"+str(i)
        i= i+1
    expr=str(coeff[0])+expr

    while (n>=3) :
        i=0
        alnaln = float(input("Input value for aln: "))
        aloalo = float(input("Input value for alo: "))
        aln=alnaln
        alo=aloalo
        condition = True
        while condition  :
                i=i+1
                b[n]=a[n]
                b[n-1]=a[n-1] + aln*b[n]
                c[n]=b[n]
                c[n-1]=b[n-1]+aln*c[n]
                j=n-2
                while(j>=0):
                    b[j]=a[j]+aln*b[j+1]+alo*b[j+2]
                    c[j] = b[j] + aln*c[j + 1] + alo*c[j + 2]
                    j-=1
                det=c[2]*c[2]-c[3]*c[1]

                if det!=0 :
                    daln = ((-1)*b[1]*c[2] + b[0]*c[3])/det
                    dalo = ((-1)*b[0]*c[2] + b[1]*c[1])/det
                    aln=aln+daln
                    alo=alo+dalo
                else :
                    i = 0
                    aln = aln+1
                    alo = alo+1

                if (((abs(daln/aln)*100 < error) & (abs(dalo/alo)*100 < error)) | (i>N)) :
                    condition = False
                    b[n] = a[n]
                    b[n - 1] = a[n - 1] + aln*b[n]
                    j = n - 2
                    while (j >= 0):
                        b[j] = a[j] + aln * b[j + 1] + alo * b[j + 2]
                        j -= 1

        n-=2
        quad_fact(aln, alo)
        j=0
        while(j<=n):

            a[j]=b[j+2]
            j= j+1

    if(n==2):
        aln=-1*a[1]/a[2]
        alo=-1*a[0]/a[2]
        quad_fact(aln,alo)
    else:
        root = (-1.0)*a[0]/a[1]
        print("Root: ","%.4f" %root)

    curveplot()


def Muller():

    coeff = []
    deg = int(input("Input degree of the polynomial: "))
    i = 0
    while (i <= deg):
        print("Input the coefficient at a[", i, "]: ")
        coeff.append((float(input(" "))))
        i = i + 1

    x0 = float(input("Guess value 1: "))
    x1 = float(input("Guess value 2: "))
    x2 = float(input("Guess value 3: "))

    error = float(input("Max relative % error: "))
    N = int(input("Max number of iterations: "))

    i = 1
    global expr
    while (i <= deg):
        expr = expr + "+" + str(coeff[i]) + "*x**" + str(i)
        i = i+1
    expr = str(coeff[0]) + expr


    i =1
    while (True):

        i = i + 1
        f0 = func(x0)
        f1 = func(x1)
        f2 = func(x2)
        diff0 = x1 - x0
        diff1 = x2 - x1
        derv0 = (f1 - f0) / diff0
        derv1 = (f2 - f1) / diff1
        a = (derv1 - derv0) / (diff1 + diff0)
        b = a * diff1 + derv1
        c = f2

        disc = math.sqrt(b * b - 4 * a * c)
        if abs(b + disc) > abs(b - disc):
            denomi = b + disc
        else:
            denomi = b - disc

        dxr = -2 * c / denomi
        xr = x2 + dxr
        # print(abs(dxr/xr)*100, " ")
        if (abs(dxr / xr) * 100 < error or i >= N):
            break
        x0 = x1
        x1 = x2
        x2 = xr

    print("The value of the root is: ", round(xr, 4));
    curveplot()

ch = int(input("Input the function used for computation\n1.Bairstow\n2.Muller : " ))
if ch==1:
    Bairstow()
elif ch==2:
     Muller()
else:
    print("Invalid")
