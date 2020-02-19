#迭代算法
import math
y0=1-1/math.e
for n in range (0,21):
    n=n+1
    y1=1-n*y0
    y0=y1
    print(y1)
    
#秦九韶算法    
import time
from functools import reduce
#reduce() 函数会对参数序列中元素进行累积

start = time.time()
def qinjiuzhao(factors,x):
    for factor in factors[1:]:
        # 使用 lambda 匿名函数
        result = reduce(lambda a,b:a*x+b,factors)
        return result
factors=(1,0,3,0,-2,6)
print(qinjiuzhao(factors,1.1))
print(qinjiuzhao(factors,1.2))
print(qinjiuzhao(factors,1.3))
end = time.time()
print(1000000*(end-start))
