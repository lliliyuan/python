import numpy as np
f = lambda x: 3 * (x ** 2) - (np.e) ** x
df = lambda x:6 * x - (np.e) ** x
#牛顿迭代法
def newton(x,f,df,e,iter):
    n=1
    while n<= iter:
        x1 = x-f(x)/df(x)
        if abs(x1-x)<e:
            return x1,n
        else:
            x=x1
            n+=1
    return None,n

# 弦截法
def xianjiefa(x0,x1,f,e,iter):
    n=1
    while n<= iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(f(x2)) < e:
            return x2,n
        else:
            n=n + 1
            x0 = x1
            x1 = x2
    return None ,n

if __name__ == "__main__":
     print(newton(-1,f,df,0.0001,100))
     print(xianjiefa(-1, 0, f, 0.0001, 1000))
     print(newton(1,f, df, 0.0001, 100))
     print(xianjiefa(0, 1, f, 0.0001, 1000))
     print(newton(3,f, df, 0.0001, 100))
     print(xianjiefa(3,4, f, 0.0001, 1000))
