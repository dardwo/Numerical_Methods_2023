def parabol(x, y, a, b):
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
        
    if (end - start) % 2 != 0:
        end += 1
        
    integral = y[start] + y[end]
    for i in range(start + 1, end, 2):
        integral += 4 * y[i]
    for i in range(start + 2, end - 1, 2):
        integral += 2 * y[i]
    integral *= h / 3
    
    return integral

x = [1, 1.5, 2, 2.5, 3]
y = [2, 5.75, 11, 17.75, 26]
#x = [0, 0.25, 0.5, 0.75, 1]
#y = [-3, -2.75, -2, -0.75, 1]

a = int(input('Enter a: '))
b = int(input('Enter b: '))

print("Approx integral = ", parabol(x, y, a, b))