import sympy as sy
import numpy as np
from sympy.functions import sin,cos

# Hello im a test comment
# Define the variable and the function to approximate
x = sy.Symbol('x')
f = x*sy.exp(-x)

# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at x0 of the function 'function'
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    return p


print(taylor(f, 0, 2));    
