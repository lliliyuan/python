def LU(A):
    n=len(A[0])
    L=np.zeros([n,n])
    U=np.zeros([n,n])
    for i in range (n):
        L[i][i]=1
        if i == 0 :
            U[0][0]=A[0][0]
            for j in range (1,n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0]/U[0][0]
        else:
            for j in range(i, n):
                temp = 0
                for k in range(0,i):
                    temp += L[i][k]*U[k][j]
                U[i][j]=A[i][j] - temp
            for j in range(i+1,n):
                temp=0
                for k in range(0,i):
                    temp += L[j][k]*U[k][i]
                L[j][i]=(A[j][i]-temp)/U[i][i]
    return L,U
if __name__ == '__main__':
    n=4
    A=[[10,-7,0,1],[-3,2.099999,6,2],[5,-1,5,-1],[2,1,0,2]]
    print('A矩阵：\n',A)
    L,U=LU(A)
    print('L矩阵：\n',L,'\nU矩阵：\n',U)
    b=np.array([8, 5.900001, 5,1])
    c=linalg.solve(L,b)
    x=linalg.solve(U,c)
    print('方程组的解：\n',x)
