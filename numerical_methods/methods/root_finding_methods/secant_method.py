import sympy as sy


def SecantMethod(function, start, end, tol, max_iter):
    x0 = start
    x1 = end

    n = 0

    while(sy.Abs(x0 - x1) > tol and n < max_iter):
        temp = sy.N(x1 - (function.subs(x, x1) * ((x1 - x0)/(function.subs(x, x1) - function.subs(x, x0))) ))
        
        x0 = x1
        x1 = temp

    return x1

x = sy.Symbol('x')
f = x**3 - x - 2
print(SecantMethod(f, 1, 2, 10**-5, 10000))
