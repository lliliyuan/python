import numpy as np
x = np.array([[10,-7,0,1],[-3,2.099999,6,2],[5,-1,5,-1],[2,1,0,2]], dtype=float)
y = np.array([8, 5.900001, 5,1], dtype=float)
f = False
def guass(x,y):
    for k in range(0,x.shape[0]-1):
        index = np.argmax(x, axis=0) #按列搜索最大值 #i 是列
        if index[k] > k:
            tmp =  x[index[k]].copy() #复制最大行
            x[index[k]] = x[k]
            x[k] = tmp #交换行
            y[index[k]] = y[k]
            y[k] = tmp
            if x[k][k] == 0:
                print("换元后矩阵主元仍含0！")
                f = True
                break

            for i in range (k+1,x.shape[0]):
                rate = x[i][k].copy() / x[k][k].copy()

                for j in range (k+1,x.shape[0]):
                    x[i][j] =x[i][j]-rate*x[k][j]
                    y[i] =y[i] -rate*y[k]
if not f:
    res = np.zeros(4)
    res[-1] = x[-1][-1]
    for i in range(x.shape[0]-1,-1,-1):
        s = y[i]
        for j in range(i + 1, x.shape[1]):
            s -= x[i][j] * res[j]
        res[i] = s / x[i][i]
    print("方程组的解\n", res)
