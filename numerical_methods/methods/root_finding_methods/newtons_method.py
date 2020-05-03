import sympy as sy

def NewtonsMethod(function, start, max_iter):
    xn = start
    n = 0
    f = function
    g = sy.diff(function)
    while(n < max_iter):
        xn = sy.N(xn - (f.subs(x, xn)/g.subs(x, xn)))
        n = n + 1
    return xn

x = sy.Symbol('x')
f = x**3 - x - 2
print(NewtonsMethod(f, 1, 10000))    

