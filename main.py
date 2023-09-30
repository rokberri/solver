from utils.io import *
from utils.ex import WrongСoefficientException
from utils.math import create_matrix, P, H, Pxy, Pyx, Hxy, H_x_y, H_y_x
import numpy as np

def solve():
    data = read_data('input.txt')
    x = int(data[0])
    y = int(data[1])
    data_coef = convert_into_float(data[2:last_ind(data)])
    try: 
        if not sum(data_coef) == 1.0:
            raise WrongСoefficientException()
    except WrongСoefficientException as er:
        print(er.txt)
        exit()
    matrix = create_matrix(x,y,data_coef)
    # print(matrix)
    p = P(matrix)
    # print(p)
    H_x = H(p[0])
    H_y = H(p[1])
    # print(Hxy(p))
    print(H_x_y(p))
    print(H_y_x(p))
    # print(H_x,H_y)
    # Pxy(matrix,p)
    # Pyx(matrix,p)

def main():
    solve()
    
if __name__ == '__main__':
    main()