import sympy as sy

def FixedPointIteration(function, start, max_iter):
    p = start
    f = function
    
    for i in range(0, max_iter):
        p = sy.N(f.subs(x, p))

    return p

x = sy.Symbol('x')
f = sy.exp(-x)
print(FixedPointIteration(f, 1, 15))



