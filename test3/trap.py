# def trap_tab():
#   y = [-3, -2.75, -2, -0.75, 1]
  
#   res = 0
#   elems = 5
#   dx = 0.25
  
#   for i in range(elems - 1):
#     res +=  ((y[i] + y[i+1]) * dx) / 2
  
#   return res

# print('res = ', trap_tab())


def trapezoidal_rule_table(x, y, a, b):
    a = x[0]
    b = x[-1]
        
    n = len(x)
    h = (x[-1] - x[0]) / (n - 1)
    
    start = 0
    while x[start] < a:
        start += 1
    end = start
    while x[end] < b:
        end += 1
        
    integral = (y[start] + y[end]) / 2
    for i in range(start + 1, end):
        integral += y[i]
    integral *= h
    
    return integral


x = [1, 1.5, 2, 2.5, 3]
y = [2, 5.75, 11, 17.75, 26]

# x = [0, 0.25, 0.5, 0.75, 1]
# y = [-3, -2.75, -2, -0.75, 1]

a = int(input('Enter a: '))
b = int(input('Enter b: '))

print("Approx integral: ", trapezoidal_rule_table(x, y, a, b))