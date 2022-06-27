# import numpy as np
import pandas as pd
from tabulate import tabulate

columns1 = [0, 1, 3, 4, 11]

data1 = pd.read_csv('11100022.csv', delimiter=',', usecols=columns1)

look_column = 'Family type'
look_text = 'Couple families'

data1 = data1[data1[look_column].str.contains(look_text)]

print(f'Статистика по {look_text}:')
print(data1.columns.tolist())
print(tabulate(data1.sample(10), headers=data1.columns.tolist()))
