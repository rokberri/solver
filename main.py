from utils.io import *
from utils.ex import WrongСoefficientException


def Solve():
    data = read_data('input.txt')
    print(data)
    x = data[0]
    y = data[1]
    data_coef = convert_into_float(data[2:last_ind(data)])
    try: 
        if not sum(data_coef) == 1.0:
            raise WrongСoefficientException()
    except WrongСoefficientException as er:
        print(er.txt)
        exit()
    print(data[2:last_ind(data)])

def main():
    