import numpy as np
import matplotlib.pyplot as plt

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('inter_inputODE.txt','r')
o = open('inter_outputODE.txt','a')
tokenized = read_by_tokens(f)
fun = str(next(tokenized))
def fu(t,y):
    return eval(fun,{}, {"t": t,"y": y})

t0 = float(next(tokenized))
s0 = float(next(tokenized))
t = float(next(tokenized))
h = float(next(tokenized))
ch = int(next(tokenized))

def curveplot(tarr,s,cur):
    plt.figure(figsize=(12, 8))
    plt.plot(tarr, s)
    plt.scatter(tarr, s, label='Approximate', color='red')
    plt.title(cur)
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.grid()
    plt.show()

def forward_euler():
    # Explicit Euler Method
    tarr=np.zeros(int(t/h)+1)
    s = np.zeros(int(t/h)+1)
    tarr[0]=t0
    s[0]=s0

    for i in range(0, len(tarr)-1):
        s[i + 1] = s[i] + h*fu(tarr[i], s[i])
        tarr[i+1]=tarr[i]+h
    print(s)
    o.write('Euler Forward\n')
    o.write("t\ty\n")
    for i in range(len(tarr)):
        o.write(str(round(tarr[i],6))+ '\t' + str(s[i]) + '\n')
    curveplot(tarr,s,'Euler Forward')

def rk_second_order():
    tarr = np.zeros(int(t / h) + 1)
    s = np.zeros(int(t / h) + 1)
    tarr[0] = t0
    s[0] = s0

    for i in range(0, len(tarr) - 1):
        k1 = h * fu(tarr[i], s[i])
        k2 = h * fu(tarr[i] + 0.5 * h, s[i] + 0.5 * k1)
        s[i+1] = s[i] +k2
        tarr[i + 1] = tarr[i] + h
    print(s)
    o.write('Runge Kutta Second Order\n')
    o.write("t\ty\n")
    for i in range(len(tarr)):
        o.write(str(round(tarr[i],6)) + '\t' + str(s[i]) + '\n')
    curveplot(tarr,s,'Runge Kutta Second Order')

def rk_fourth_order():
    tarr = np.zeros(int(t / h) + 1)
    s = np.zeros(int(t / h) + 1)
    tarr[0] = t0
    s[0]=s0
    # Iterate for number of iteration
    for i in range(0, len(tarr) - 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * fu(tarr[i], s[i])
        k2 = h * fu(tarr[i] + 0.5 * h, s[i] + 0.5 * k1)
        k3 = h * fu(tarr[i] + 0.5 * h, s[i] + 0.5 * k2)
        k4 = h * fu(tarr[i] + h, s[i] + k3)
        s[i+1] = s[i] + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        tarr[i + 1] = tarr[i] + h
    print(s)
    o.write('Runge Kutta Fourth Order\n')
    o.write("t\ty\n")
    for i in range(len(tarr)):
        o.write(str(round(tarr[i],6)) + '\t' + str(s[i]) + '\n')

    curveplot(tarr,s,'Runge Kutta Fourth Order')



if ch==1:
    forward_euler()
if ch==2:
    rk_second_order()
if ch==3:
    rk_fourth_order()
f.close()
o.close()