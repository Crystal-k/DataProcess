import pandas as pd
import os

data = pd.read_csv('./source_data/evo_test.csv', encoding='utf-8')
with open('./target_data/evo_test.txt', 'w', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + ' ' + str(line[3]) + ' ' + str(line[4]) + ' ' + str(line[5]) + ' ' + str(line[6]) + ' ' + str(line[7]) +'\n'))