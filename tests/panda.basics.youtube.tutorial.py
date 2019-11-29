import numpy as np # dependency for pandas

import pandas as pd
def header(msg): # dummy heather. what it is used for?
    print('-' * 50)
    print('['+ msg + ']')

#1 load hard-coded data into a datafram
#header ("1. load hard - coded data into  a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

#2 read text file into a DataFrame
header("2. read text file into a df")
filename = "/Users/larryeverson/Desktop/Immigration_post_1991_latest/data/Fremont_weather.csv"
df = pd.read_csv(filename)
print(df)

#3 print 5 or last 3 row of data DataFrame
header("3. df.head()")
print(df.head()) # it automatically gives you the first 5 lines
header("3.df.tail(3)")
print(df.tail(3))

#4 get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header ("4. df.values")
print(df.values)

# 5. statistical summary of each columns
header("5. df.describe()")
print(df.describe())

# 6. sort record by any column
header ("6. df.sort_values('record high,ascending = False)")
print(df.sort_values('record_high', ascending = False))

# Note, even if we delete "ascending = False", the data will still be dispayed in the descending  order

# 7. slicing records
header("7. slicing -- df.avg_low") # index with singel column
print(df.avg_low)

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header(" 7. slicing -- df[2:4]") # index with a single column
print(df[2:4]) # rows 2 to 3

header ("7. slicing -- df[['avb_low','avg_hight']]")
print(df[['avg_low','avg_high']])

header ("7. slicing --df.loc[:,['avg_low','avg_high']]") # location can tak 4 paramether
print(df.loc[:,['avg_low', 'avg_high']]) #: colon means that we all values are included
# multiple columns: df.loc[from_row:to_row,['comlumn1','column2']]

header ("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header ("7.df.iloc[3:5,[0,3]]")#Not working
# index location can receive range or lists of indices
#print(df_iloc[3:5,[0,3]])

# 8. filtering
header("8.df[df.avg_precipitation > 1.0]") # filter on column values
print(df[df.avg_precipitation > 1.0]) # anythign that will return a boolean

header ("8. df[df['month']. isin['Jun','Jul', 'Aug']]")
print(df[df['month'].isin(["Jun","Jul", "Aug"])])

# 9. assignment -- very similar to slicing
header ("9.df.loc[9,['avg_precipitation']] = 101.3") # assign a single scala value to one cell
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header ("9. df.loc[9,['avg_precipitation']] = np.nan")
# handles missing data. Eliminates the need for exception handling. It will skip that row
df.loc[9,['avg_precipitation']] = np.nan # will assing nan to row 9 to see how it looks
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5])* len(df)")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] =(df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace = True)")
df.rename(columns = {'avg_precipitation':'avg_rains'}, inplace = True) # rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi', 'rec_lo','av_rain']")
#df.columns = ['month','av_hi','av_lo','rec_hi', 'rec_lo','av_rain']
#print(df.head())
print('Print: ValueError: Length mismatch: Expected axis has 7 elements, new values have 6 elements')
#code not working properly
#11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print(index, row["month"], row["avg_high"])

#12. write to csf file
df.to_csv('foo.csv')



##############################
#Error Log
#In task 2,
    #2.1 learned to access the data post in githum in RAW version, save it to my computer in cvs format.
    # 2.2 saved the file as: csv in project folder
    #2.2 copy the full path of the data into the project by doing a right click
