# Numerical_Methods_2023


1. Cubic Interpolation


The code above implements the natural cubic spline interpolation method to interpolate a set of given data points. It constructs a set of cubic polynomials that interpolate the data points and has continuous first and second derivatives at each data point.

The `natural_cubic_spline` function takes two arguments `X` and `Y`, which are the arrays of the x and y values of the data points. The function returns a list of lambda functions, where each lambda function is a cubic polynomial that interpolates the data points between consecutive x values.

The `si` function is an auxiliary function that computes the value of the cubic polynomial that interpolates the data points between the i-th and (i+1)-th x values.

The code then uses Sympy to print out the analytical form of each of the cubic polynomials. The `Si_analytical` variable contains the symbolic expression for the i-th cubic polynomial. The `sp.printing.latex` function is used to print the expression in LaTeX format.

Note that the `natural_cubic_spline` function assumes that the x values in the `X` array are in increasing order. The function also assumes that the x values are equally spaced. If the x values are not equally spaced, the function can be modified by using the `np.diff` function to compute the differences between the x values instead of assuming that they are equal.

Also note that the `natural_cubic_spline` function uses the `np.linalg.solve` function to solve the system of linear equations for the coefficients of the cubic polynomials. This may be slow for large datasets, and other methods such as LU decomposition or Cholesky decomposition may be faster.

2. Trapezoidal Rule & Simpson Rule


This code defines two functions, `trapezoidal_rule` and `simpsons_rule`, which calculate an approximate definite integral of a given function `f` using the trapezoidal rule and Simpson's rule, respectively. 

`trapezoidal_rule` uses the trapezoidal rule, which approximates the area under a curve between two points as the area of the trapezoid formed by connecting the two points with a straight line. It takes four arguments: the function `f`, the limits of integration `a` and `b`, and the number of subintervals `n` to use in the approximation. It calculates the step size `h` as `(b - a) / n`, and then calculates the approximate integral as the sum of the function values at the endpoints and midpoints of the subintervals, multiplied by `h / 2`.

`simpsons_rule` uses Simpson's rule, which approximates the area under a curve between two points as the area of a parabolic segment that passes through the endpoints and midpoint of the interval. It takes the same four arguments as `trapezoidal_rule`, and additionally checks if the number of subintervals is even. It calculates the step size `h` in the same way as `trapezoidal_rule`, and then calculates the approximate integral as the sum of the function values at the endpoints, midpoints, and quarterpoints of the subintervals, multiplied by appropriate coefficients.

The code then defines a function `f(x)` which returns the value of `x^2 * cos(x)`, sets the limits of integration `a` and `b` to `0` and `pi`, respectively, and sets the number of subintervals `n` to `20`. It calculates the approximate integrals using both methods and prints the results to the console.


