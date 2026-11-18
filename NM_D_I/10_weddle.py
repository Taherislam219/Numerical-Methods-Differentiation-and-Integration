
import math

def f(x):
    return 1 / (1 + x**2)

a, b = 0, 1
n = 6
h = (b - a) / n
y = [f(a + i * h) for i in range(n + 1)]

if n % 6 != 0:
    print("n must be a multiple of 6")
else:
    coef = [1, 5, 1, 6, 1, 5, 1]
    I = 0
    for i in range(0, n, 6):
        for j in range(7):
            I += coef[j] * y[i + j]
    I = 3 * h / 10 * I
    print("Weddle =", I)
