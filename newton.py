def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-14:
            raise ValueError("Derivada cercana a cero.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

f = lambda x: x**(1/3)
df = lambda x: 1/(3*x**(2/3))
raiz, iteraciones = newton_raphson(f, df, 1.0)
print("Raíz:", raiz)
print("Iteraciones:", iteraciones)
