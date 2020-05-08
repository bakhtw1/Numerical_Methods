import sympy as sy
import numpy as np
import sys

def NewtonsPolynomial(point_data):
    n = len(point_data)
    div_diff = np.zeros((n, n), dtype=float)
    GenerateDividedDifferences(0, n-1, point_data, div_diff)
    x = sy.Symbol('x')
    f = point_data[0][1]

    for i in range(1, n):
        g = 1
        for j in range(0, i):
            g = g*(x - point_data[j][0])
        f = f + (div_diff[0][i]*g)

    print(f)

    return div_diff

    
def GenerateDividedDifferences(in1, in2, p_data, mat):
    result = 0
    if(in2 - in1 == 1):
        result = (p_data[in2][1] - p_data[in1][1])/(p_data[in2][0] - p_data[in1][0])
        mat[in1][in2] = result
    elif(in2 - in1 > 1):
        result = (GenerateDividedDifferences(in1 + 1, in2, p_data, mat) - GenerateDividedDifferences(in1, in2 - 1, p_data, mat))/(p_data[in2][0] - p_data[in1][0])
        mat[in1][in2] = result
    else:
        # error case not allowed
        # implies cases where in1 > in2
        # may cause divide by zero error
        print("Error")
        sys.exit()

    return result


    

def DividedDifference(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])


data = [(1,2),(3,4),(5,7),(2,4),(6,3),(-1,2),(-2,4),(10,4),(7,-3)]
test = NewtonsPolynomial(data)
print(test)   