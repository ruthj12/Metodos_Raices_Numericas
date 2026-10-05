def biseccion(f, a, b, tol=1e-5, max_iter=1000):
    if f(a) == 0:
        return a, 0
    if f(b) == 0:
        return b, 0
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en [a,b].")

    for i in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)

        if abs(fm) < tol or abs(b - a) < tol:
            return m, i

        if f(a) * fm < 0:
            b = m
        else:
            a = m

    return (a + b)/2, max_iter


f = lambda x: x**3 - 7*x + 6
raiz, iteraciones = biseccion(f, 0, 2)
print("Raíz:", raiz)
print("Iteraciones:", iteraciones)
