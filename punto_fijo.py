def punto_fijo(g, x0, tol=1e-5, max_iter=1000):
    x = x0
    for i in range(max_iter):
        xn = g(x)
        if abs(xn - x) < tol:
            return xn, i + 1
        x = xn
    return x, max_iter

g1 = lambda x: 2.718281828459045**(-x)
x0 = 1.0
raiz, it = punto_fijo(g1, x0)
print("Raíz:", raiz)
print("Iteraciones:", it)
