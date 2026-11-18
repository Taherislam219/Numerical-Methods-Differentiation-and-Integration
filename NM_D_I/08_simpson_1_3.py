
import math

def f(x):
    return 1 / (1 + x**2)

a, b = 0, 1
n = 6
h = (b - a) / n
y = [f(a + i * h) for i in range(n + 1)]

if n % 2 != 0:
    print("n must be even")
else:
    I = y[0] + y[n]
    for i in range(1, n):
        if i % 2 == 1:
            I += 4 * y[i]
        else:
            I += 2 * y[i]
    I = h / 3 * I
    print("Simpson 1/3 =", I)
