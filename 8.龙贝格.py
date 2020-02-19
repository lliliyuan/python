#  龙贝格法求积分
import math
a=0             # 积分下限
b=1            # 积分上限
eps=10**-3   # 精度
T=[]            # 复化梯形序列
S=[]            # Simpson序列
C=[]            # Cotes序列
R=[]            # Romberg序列
def func(x):    # 被积函数
    y=math.sin(x)
    return y
def Romberg(a,b,eps,func):
    h = b - a
    T.append(h * (func(a) + func(b)) / 2)
    ep=eps+1
    m=0
    while(ep>=eps):
        m=m+1
        t=0
        for i in range(2**(m-1)-1):
            t=t+func(a+(2*(i+1)-1)*h/2**m)*h/2**m
        t=t+T[-1]/2
        T.append(t)
        if m>=1:
            S.append((4**m*T[-1]-T[-2])/(4**m-1))
        if m>=2:
            C.append((4**m*S[-1]-S[-2])/(4**m-1))
        if m>=3:
            R.append((4**m*C[-1]-C[-2])/(4**m-1))
        if m>4:
            ep=abs(10*(R[-1]-R[-2]))
Romberg(a,b,eps,func)
# print(T)
# print(S)
# print(C)
# print(R)
print("积分结果为：{:.5f}".format(R[-1]))
