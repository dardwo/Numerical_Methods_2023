import numpy as np
import sympy as sp

def natural_cubic_spline(X, Y):
    n = len(X)
    h = np.diff(X)
    A = np.zeros((n, n))
    b = np.zeros((n, 1))
    
    for i in range(1, n-1):
        A[i, i-1:i+2] = [h[i-1], 2*(h[i-1]+h[i]), h[i]]
        b[i] = 3 * ((Y[i+1]-Y[i])/h[i] - (Y[i]-Y[i-1])/h[i-1])
    
    A[0, 0] = 1
    A[n-1, n-1] = 1
    
    c = np.linalg.solve(A, b)
    b = np.zeros((n-1, 1))
    d = np.zeros((n-1, 1))
    
    for i in range(n-1):
        b[i] = (Y[i+1]-Y[i])/h[i] - h[i]*(2*c[i]+c[i+1])/3
        d[i] = (c[i+1]-c[i])/(3*h[i])
    
    def si(x, i):
        return Y[i] + b[i]*(x-X[i]) + c[i]*(x-X[i])**2 + d[i]*(x-X[i])**3
    
    S = []
    for i in range(n-1):
        S.append(lambda x, i=i: si(x, i))
    
    return S


X = np.array([ 1, 2, 3, 4])
Y = np.array([1,1,0,10])

S = natural_cubic_spline(X, Y)
    

x = sp.symbols('x')

for i in range(len(S)):
    Si_analytical = sp.expand(sp.Matrix(S[i](x))[0,0])
    print(f"S{i}(x) = {sp.printing.latex(Si_analytical)}")