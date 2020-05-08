import sympy as sy
import sys

def GetBasisFunctions(point_data):
    x = sy.Symbol('x')
    n = len(point_data)
    result = []

    for i in range(0, n):
        f = 1
        for j in range(0, n):
            if(i != j):
                if((point_data[i][0] - point_data[j][0]) == 0):
                    print("Divide by Zero Error, Not a Function")
                    sys.exit(0)
                f = f * ((x - point_data[j][0])/(point_data[i][0] - point_data[j][0]))
        
        result.append(f)

    return result

def LagrangeInterpolation(point_data):
    n = len(point_data)
    result = 0

    basisFunctions = GetBasisFunctions(point_data)

    for i in range(0, n):
        result = result + point_data[i][1]*basisFunctions[i]

    return result
