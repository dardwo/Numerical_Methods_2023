""" This function solves a nonlinear equation f(x) = 0 using the secant method. """

def secant_method(f_str, x0, x1, tol, max_iter):
    
    # creates lambda function f that takes a single argument x 
    f = lambda x: eval(f_str)
    
    i = 0
    while abs(f(x1)) > tol and i < max_iter:
        x2 = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        x0, x1 = x1, x2
        i += 1
    return x2

# input the function
f_str = input("Enter the function f(x): ")

# input the initial guesses
x0 = float(input("Enter the initial guess x0: "))
x1 = float(input("Enter the initial guess x1: "))

# input the tolerance
tol = float(input("Enter the tolerance: "))

# input the maximum number of iterations
max_iter = int(input("Enter the maximum number of iterations: "))

root = secant_method(f_str, x0, x1, tol, max_iter)
print(root)