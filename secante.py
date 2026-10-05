def secante(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1 - fx0) < 1e-14:
            raise ValueError("Denominador casi cero.")

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        if abs(x2 - x1) < tol:
            return x2, i + 1

        x0, x1 = x1, x2

    return x1, max_iter

f = lambda x: __import__("math").cos(x) - x
raiz, it = secante(f, 0, 1)
print("Raíz:", raiz)
print("Iteraciones:", it)
