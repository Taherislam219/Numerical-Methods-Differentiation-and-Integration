
def f(x, y):
    return x + y

x0, y0 = 0, 1
h = 0.1
xn = 0.5
n = int(round((xn - x0) / h))

x, y = x0, y0
print(f"x = {x:.2f}, y = {y:.6f}")

for i in range(n):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h/2 * k1)
    y = y + h * k2
    x = x + h
    print(f"x = {x:.2f}, y = {y:.6f}")
