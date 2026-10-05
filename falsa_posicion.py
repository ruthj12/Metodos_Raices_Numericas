def falsa_posicion(f, a, b, tol=1e-5, max_iter=1000):
    if f(a) == 0:
        return a, 0
    if f(b) == 0:
        return b, 0
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en [a,b].")

    for i in range(1, max_iter + 1):
        x = b - f(b) * (b - a) / (f(b) - f(a))
        fx = f(x)

        if abs(fx) < tol:
            return x, i

        if f(a) * fx < 0:
            b = x
        else:
            a = x

    return x, max_iter

f = lambda x: x**3 + x**2 - 1
raiz, iter = falsa_posicion(f, 0, 1)
print("Raíz:", raiz)
print("Iteraciones:", iter)
