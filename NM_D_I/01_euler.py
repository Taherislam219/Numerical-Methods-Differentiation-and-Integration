
def f(x, y):
    return x + y

x0, y0 = 0, 1
h = 0.1
xn = 0.5
n = int(round((xn - x0) / h))

x, y = x0, y0
print(f"x = {x:.2f}, y = {y:.6f}")

for i in range(n):
    y = y + h * f(x, y)
    x = x + h
    print(f"x = {x:.2f}, y = {y:.6f}")
