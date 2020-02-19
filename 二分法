#求根画图
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(3,5,100)
f =3*(x**2)-(np.e)**x

plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,f,color="b",linestyle="-",lw=2.5,label="f(x)")
plt.legend()
plt.xticks(range(-5,5,1))
plt.grid(True,linestyle='-', alpha= 0.5)
plt.show()

#二分法
def erfenfa(fun, start, end, precision):
    s = fun(start)
    e = fun(end)
    if e*s > 0:
        #print("No solution!")
        return False
    if s == 0:
        print("Solution is ",start)
        return start
    if e == 0:
        print("Solution is ",end)
        return end
    while abs(end - start) > precision:
        mid = (start + end)/2.0
        m = fun(mid)
        if m == 0:
            print("Solution is ", mid)
            return mid
        if s*m < 0:
            end = mid
        if m*e < 0:
            start = mid
    print("Solution is ",start)
    return start

def func(x):
    return (5*x**2)*(np.sin(x))-(np.e)**(-x)

if __name__ == "__main__":
    for start in range(-5,100):
        end=start+1
        val = erfenfa(func, start, end, 0.0001)
    print("Result is ", func(val))
