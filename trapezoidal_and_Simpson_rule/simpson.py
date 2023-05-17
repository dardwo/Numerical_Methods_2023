import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    integral *= h / 3
    return integral


def f(x):
    return x**2 * math.cos(x)

a, b = 0, math.pi
n = 20

integral_trapezoidal = trapezoidal_rule(f, a, b, n)
integral_simpsons = simpsons_rule(f, a, b, n)

print("Trapezoidal rule: ", integral_trapezoidal)
print("Simpson's rule: ", integral_simpsons)