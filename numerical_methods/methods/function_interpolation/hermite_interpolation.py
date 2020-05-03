import sympy as sy
import sys 
import lagrange_interpolation as li

def HermiteInterpolation(function, x_point_data, sym):
    x = sy.Symbol(sym)
    f = function
    g = sy.diff(function)
    n = len(x_point_data)
    point_data = []
    result = 0*x

    for i in range(0, n):
        point_data.append((x_point_data[i],f.subs(x, x_point_data[i])))

    basis_functions = li.GetBasisFunctions(point_data)

    for i in range(0, n):
        diff_basis = sy.diff(basis_functions[i])
        result = result + (1 - 2 * (x - point_data[i][0]) * diff_basis.subs(x, point_data[i][0])) * (basis_functions[i]**2) * point_data[i][1]
    
    for i in range(0, n):        
        result = result + (x - point_data[i][0])*(basis_functions[i]**2)*g.subs(x, point_data[i][0])

    return result

x = sy.Symbol('x')
print(HermiteInterpolation(sy.ln(x), [1,2,3], 'x'))    
