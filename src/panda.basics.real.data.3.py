import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import os

# generate the year diapason
years = list(range(2011,2019))


filename = '3. Imigranti dupa tara de emigrare si scopul sosirii , 2011-2018.csv'
filepath = f"{os.getcwd()}/data/real/{filename}"

# FIRST - the files contain corrupt CSV format - double double quotes which prevent reading the columns correctly
# we replace them
# we then open the FIXED file
# fin = open(filepath, "rt")
# fout = open(filepath + "_fixed.csv", "wt")
# for line in fin:
# 	fout.write(line.replace('""', '').replace('"',''))
# fin.close()
# fout.close()



df = pd.read_csv(filepath + "_fixed.csv", index_col=0, sep=";",
                 skiprows=2,
                 # quotechar="\""
                 ###, names=['nationality'] + colum_names
                 )

# FIX: we replace not numeric values with 0 - int so calculations could be done
df = df.replace('-0',0).replace('-',0) 


# we convert the data set to int32 (which is enought precision for needed calculations)

# print(df)
# print(df.columns)


total_total_data = df.loc[:, [
    f"{year} Total" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_work_data = df.loc[:, [
    f"{year} La munca" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_study_data = df.loc[:, [
    f"{year} La studii" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_family_data = df.loc[:, [
    f"{year} Imigratie de familie" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_humanitary_data = df.loc[:, [
    f"{year} Activitati religioase, umanitare si de voluntariat" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

# FIX - commas
# total_other_data = df.loc[:, [f"{year} Alte cauze/ motive" for year in years]].replace(r'[^0-9]', '') #.astype('int32').sum(axis=1).loc['Tara de emigrare-total']
# the column - Other motifs - doesnt load well cause it's malformed, but we will calculate itl below using substraction ;)

print(total_total_data)
print(total_work_data)
print(total_study_data)
print(total_family_data)
print(total_humanitary_data)
total_other_data = total_total_data - (total_work_data +
                                         total_study_data +
                                         total_family_data +
                                         total_humanitary_data)
print(total_other_data) 

# exit()

############ PREPARE  ############################
data = pd.DataFrame({'Immigrants % of total': [
                            total_work_data/total_total_data,
                            total_study_data/total_total_data,
                            total_family_data/total_total_data,
                            total_humanitary_data/total_total_data,
                            total_other_data/total_total_data,
                    ]},
                    index=[f'Work {round(100*total_work_data/total_total_data)}%', f'Study {round(100*total_study_data/total_total_data)}%', f'Family{round(100*total_family_data/total_total_data)}%', f'Humanitary and Religious {round(100*total_humanitary_data/total_total_data)}%', f'Other motifs {round(100*total_other_data/total_total_data)}%'])
############ PLOT & SAVE #########################
data.plot(kind='pie', figsize=(7, 7), subplots=True)
plt.savefig(filepath + "__3-A.png")
plt.title("Total immigrants by purpose")
plt.show()




