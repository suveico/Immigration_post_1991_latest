import numpy as np  
import pandas as pd
import os

def header(msg):
    print('-' * 50)
    print('['+ msg + ']')

filename = f"{os.getcwd()}/data/real/imigr._scop_tara_2001-2010.xlsx"
df = pd.read_excel(filename, index_col=0)
print(df)

header(" 1.Data type 'type.(df)'")
print(type(df)) # class 'pandas.'

#you should see <class 'pandas.core.frame.DataFrame'> which means
# that you get an object of type "DataFrame" and you can use all of it's options / methods

header(" 2.Columns 'df.columns'")
print(df.columns)


header(" 3.Slicing the rows and columns by index location 'df.iloc[5:146, [0]") # column index 0-4 inclusive
useful_data = df.iloc[5:146,[0]] # assigne it to varialbe useful_data
print( useful_data )
print( useful_data.columns )
print( type( useful_data ) )

header("4. Rename Unnamed:1 column to  2001  ->.rename(columns={ 'Unnamed: 1': '2001'})")
useful_data = useful_data.rename(columns={ 'Unnamed: 1': '2001'})
print( useful_data )

header(" 5. Replace strings with 0 (.replace('-',0)) and Sort in descd. ord (sort_values('2001', ascending = False ) ")
useful_data = useful_data.replace('-', 0).sort_values( '2001', ascending = False )
print( useful_data )

header("6. Print the first 10 rows '.head(10)' ")
useful_data = useful_data.head(10)
print( useful_data )

header("7. Save file into csv file")
filename = f"{os.getcwd()}/data/real/top_10_2001.csv"
useful_data.to_csv(filename)


#####
#Error Log
# ROOT level of the project gives you access to all the folders inside
# df = pd.read_excel(filename, index_col=0) we specify col 0(country names) to be index
# iloc takes two paramethers( row location), (column location)
# when changing the column location, Notice that the Unnamed column also needs to be changed to whatever new Unnamed column
