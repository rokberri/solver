import numpy as np
from numpy import ndarray


def P(matrix:ndarray):
    return (matrix.sum(1, dtype='float'),matrix.sum(0, dtype='float'))

def H(data):
    result = 0
    for el in data:
        result+= el * np.log2(el)
    return abs(result)

def Hxy(p):
    result = 0.0
    for i in p:
        for j in i:
            result += j * np.log2(j)
    return abs(result)

def  H_x_y(p):
    result = 0
    for i in p[1]:
        result += i*H(p[1])
    return result

def  H_y_x(p):
    result = 0
    for i in p[0]:
        result += i*H(p[0])
    return result

def Pxy(matrix,p):
    for row in matrix: 
        ind = 0
        for el in row:
            print(el/p[1][ind])
            ind+=1
def Pyx(matrix,p):
    for row in matrix: 
        ind = 0
        for el in row:
            print(el/p[0][ind])
            ind+=1

def create_matrix(x:int,y:int,data)->ndarray:
    matrix = np.array(data).reshape(x,y)
    return matrix