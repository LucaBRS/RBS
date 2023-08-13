import pandas as pd
import numpy as np
import os

def clean_dataset(dataset):
    print('start cleaning')

    for i in dataset:
        dataset[i] = dataset[i][ dataset[i]['electrosmog'].astype(str).__contains__('-') == False ]
        i.to_csv('./clean_file/'+str(i))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = './resources/'

    dir_list = os.listdir(path)
    pool = {}
    for file in dir_list:
        if file.endswith('.csv'):
            print(file.split('.')[0].split('_')[1].replace('0', '') + '_' + file.split('.')[0].split('_')[0])
            pool[file.split('.')[0].split('_')[1].replace('0', '') + '_' + file.split('.')[0].split('_')[
                0]] = pd.read_csv(path + file, sep=';', engine='python')
# CAP133_1
# CAP153_1
# CAP133_2
# CAP153_2
# CAP133_3
# CAP153_3
    clean_dataset(pool)



