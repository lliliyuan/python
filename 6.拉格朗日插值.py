import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x=[0,1,4,9,16,25,36,49,64]
y=[0,1,2,3,4,5,6,7,8]
def f(x):
    return 1.0/(1+x**2)
def Lagrange(xi,yi):
    n=len(xi)
    m=len(yi)
    if n==m:
        p=np.poly1d([0])
        for k in range(n):
            L=np.poly1d([1])
            for i in range(n):
                if i != k:
                    L=L*np.poly1d([1.0/(xi[k]-xi[i]),-float(xi[i])/(xi[k]-xi[i])])
            p=p+yi[k]*L
    return p
for n in range(2,15):
    x=np.linspace(-5 , 5, n)
    y=f(x)
    xx=np.linspace(-5 , 5, 200)
    yy=f(xx)
    p =Lagrange(x,y)
    y1=p(xx)
    plt.figure(figsize=(20,8))
    plt.plot(x,y,"o",xx,y1,"r",xx,yy,"b",label = "插值数为：n")
    plt.legend()
    plt.grid(True)
    plt.show()
