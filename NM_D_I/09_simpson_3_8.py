
import math

def f(x):
    return 1 / (1 + x**2)

a, b = 0, 1
n = 6
h = (b - a) / n
y = [f(a + i * h) for i in range(n + 1)]

if n % 3 != 0:
    print("n must be a multiple of 3")
else:
    I = y[0] + y[n]
    for i in range(1, n):
        if i % 3 == 0:
            I += 2 * y[i]
        else:
            I += 3 * y[i]
    I = 3 * h / 8 * I
    print("Simpson 3/8 =", I)
