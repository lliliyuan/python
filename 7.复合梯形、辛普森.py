import math
#复合梯形公式
def tixing(f,a,b,n):
    x=a
    h=(b-a)/n
    s=f(x)+f(b)
    for k in range(0,n):
        x=x+h
        s=s+2*f(x)
    result=(h/2)*s
    return result

#复合辛普森公式
def simprson(f,a,b,n):
    """ f被积函数，a,b分别为积分的上下线，n为子区间的个数，s是梯形总面积"""
    h = (b-a)/n
    x=a
    s=f(x)+f(b)
    for k in range (0,n):
        x=x+h/2
        s=s+4*f(x)
        x=x+h/2
        s=s+2*f(x)
    result = (h/6)*s
    return result

if __name__ == '__main__':
    n=100
    n1=1000
    f=lambda x :math.sin(x)
    print(tixing(f, 0, 1, n))
    print(simprson(f, 0, 1, n))
    print(tixing(f, 0, 1, n1))
    print(simprson(f, 0, 1, n1))
