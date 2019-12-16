import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import os


colum_names = [str(i) for i in range(1993, 2019, 1)]

filename = '1_Imigranti dupa nationalitate_1993-2018.csv'
filepath = f"{os.getcwd()}/data/real/{filename}"
# FIX: we set forced delimiter (cause by default it will read comma)
# FIX: we skip first 3 rows cause the file is malformed 
# FIX: we also generate the column names (1993..2018) cause the file is malformed 
df = pd.read_csv(filepath, index_col=0, sep=";",
                 skiprows=3, names=['nationality'] + colum_names)
# FIX: we replace not numeric values with 0 - int so calculations could be done
df = df.replace('-0',0).replace('-',0) 



# we convert the data set to int32 (which is enought precision for needed calculations)
total_by_nationality_data = df.loc[:, colum_names].astype('int32').sum(axis=1).sort_values(0,ascending=False).head(20)
print(total_by_nationality_data.index)



############ PLOT & SAVE #########################
total_by_nationality_data.plot(kind='bar', figsize=(15, 15))
plt.savefig(filepath + "__1-A.png")
plt.title("Total top 20 immigrants by nationality")
plt.show()


