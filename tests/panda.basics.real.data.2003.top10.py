import numpy as np  # dependency for pandas
import pandas as pd
import os


def header(msg):
    print('-' * 50)
    print('['+ msg + ']')
# read from xlsx
filename = f"{os.getcwd()}/data/real/imigr._scop_tara_2001-2010.xlsx"
df = pd.read_excel(filename, index_col=0)
#print(df)

# save as csv
filename = f"{os.getcwd()}/data/real/top_10_2003.csv"

# find top 10 countrie
useful_data = df.iloc[5:146,[8]].rename(columns={ 'Unnamed: 9': '2003'}).replace('-', 0).sort_values( '2003', ascending = False ).head(10).to_csv(filename)
print(useful_data)
