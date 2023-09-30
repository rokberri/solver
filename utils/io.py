def read_data(path:str):
    data = list()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data

def convert_into_float(data:list)->list[float]:
    float_data = list()
    for s in data: 
        for el in s.split(' '):
            float_data.append(float(el))
    return float_data

def last_ind(data)->int:
    return len(data)
