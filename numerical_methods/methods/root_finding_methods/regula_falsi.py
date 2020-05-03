import sympy as sy

x = sy.Symbol('x')
f = x**3 - x - 2

def RegulaFalsi(function, start, end, tol, max_iter):

    a = start
    b = end
    n = 0
    c = 0

    while(sy.Abs(a-b) > tol and n < max_iter):
        c = sy.N(b - function.subs(x, b) * ((b - a)/( function.subs(x, b) - function.subs(x, a) )))
        
        if(function.subs(x, c) * function.subs(x, a) > 0):
            a = c
        else:
            b = c

        n = n + 1

    return c

print(RegulaFalsi(f, 1, 2, 10**-5, 100000))
