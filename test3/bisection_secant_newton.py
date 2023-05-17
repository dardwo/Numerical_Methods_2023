import math

def f(x):
    return math.sin(x) - x/2 + 1/2
    # return x**3 - 12*x**2 + 3*x +1

def df(x):
    return math.cos(x) - 1/2
    # return 2*x**2 - 24*x + 3

def bisection_method(f, a, b, tol, max_iter):
    
    i = 0
    while abs(b - a) > tol and i < max_iter:
        c = (a + b)/2
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
        i += 1
    print('itreations =', i)
    # print('f(root) =', f(c))
    return c

def secant_method(f, x0, x1, tol, max_iter):
    
    i = 0
    while abs(f(x1)) > tol and i < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0, x1 = x1, x2
        i += 1
        
    print('iterations =', i)
    # print('f(root) =', f(x2))
    return x2

def newton_method(f, df, x0, tol, max_iter):
    i = 0
    while abs(f(x0)) > tol and i < max_iter:
        x1 = x0 - f(x0)/df(x0)
        x0 = x1
        i += 1

    print('iterations = ', i)
    # print('f(root) =', f(x1))
    return x1

x0 = float(input("Enter the x0: "))
x1 = float(input("Enter the x1: "))

# tolreance: 1e-6 = 1 * 10**(-6) = 0.000001
tol = float('1e-10')

# max_iterations = int(input("Enter the maximum number of iterations: "))
max_iter = 300

print('\nBISECTION')
print('root =', bisection_method(f, x0, x1, tol, max_iter))
print('\nSECANT')
print('root =', secant_method(f, x0, x1, tol, max_iter))
print("\nNEWTON")
print('root =', newton_method(f, df, x0, tol, max_iter))