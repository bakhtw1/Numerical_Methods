import sympy as sy

x = sy.Symbol('x')
f = x**3 - x - 2

def BisectionMethod(function, start, end, tol, max_iter):
    a = start
    b = end
    n = 0
    c = 0
    print(sy.Abs((b-a)/2), 10**-5)
    while( sy.Abs((b-a)) > tol and n < max_iter ):
        c = (a + b) / 2
        
        if(function.subs(x, c) == 0):
            return c

        if((function.subs(x, a) * f.subs(x, c)) > 0):
            a = c
        else:
            b = c

        print(n) 
        n =  n + 1
    
    return c

print(BisectionMethod(f, 1, 2, 10**-5, 100000))