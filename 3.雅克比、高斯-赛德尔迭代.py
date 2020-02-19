#雅克比迭代法
import numpy as np
def jacobi(A,b,J,e,iter):
    n=1
    while n<=iter:
        D = np.diag(np.diag(A))
        L = np.tril(A, -1)
        U = np.triu(A, 1)
        d= np.linalg.inv(D)
        B = np.dot(d, -(L + U))
        f = np.dot(d, b)
        X = np.dot(B, J) + f
        if np.linalg.norm(X-J)<e:
            return X,n
        else:
            n=n+1
            J = X
            X = np.dot(B, J) + f
    return None,n

#高斯-赛德尔迭代法
def GS(A,b,J,e,iter):
    n = 1
    while n <= iter:
        D = np.diag(np.diag(A))
        L = np.tril(A, -1)
        U = np.triu(A, 1)
        d = np.linalg.inv(D+L)
        B = np.dot(d, -U)
        f = np.dot(d, b)
        X = np.dot(B, J) + f
        if np.linalg.norm(X - J) < e:
            return X, n
        else:
            n = n + 1
            J = X
            X = np.dot(B, J) + f
    return None, n


if __name__ == "__main__":
    A = [[10,-1,-2],
        [-1,10,-2],
        [-1,-1,5]]
    b = [72,83,42]
    J = [0,0,0]
    print(jacobi(A,b,J,0.00001,100))
    print(GS(A,b,J,0.0001,100))


