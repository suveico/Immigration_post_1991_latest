import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import os

# generate the year diapason
years = list(range(2014,2018))


filename = '4. Emigranti si imigranti in baza traversarilor frontierei de stat_pe sexe si grupe de virsta_2014-2017.xlsx'
filepath = f"{os.getcwd()}/data/real/{filename}"

df = pd.read_excel(filepath, index_col=0, sep=";",
                 skiprows=2,
                 # quotechar="\""
                 ###, names=['nationality'] + colum_names
                 )

print(df)
print(df.columns)


total_immigr_total_data = df.loc[:, [
    f"{year}" for year in years]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

total_immigr_men_data = df.loc[:, [
    f"Unnamed: {n}" for n in range(2, 24, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

total_immigr_women_data = df.loc[:, [
    f"Unnamed: {n}" for n in range(3, 25, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

total_emmigr_total_data = df.loc[:, [
    f"Unnamed: {n}" for n in range(4,28,6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

total_emmigr_men_data = df.loc[:, [
    f"Unnamed: {n}" for n in range(5, 29, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

total_emmigr_women_data = df.loc[:, [
    f"Unnamed: {n}" for n in range(6, 30, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

# FIX - commas
# total_other_data = df.loc[:, [f"{year} Alte cauze/ motive" for year in years]].replace(r'[^0-9]', '') #.astype('int32').sum(axis=1).loc['Tara de emigrare-total']
# the column - Other motifs - doesnt load well cause it's malformed, but we will calculate itl below using substraction ;)
print(total_immigr_total_data)
print(total_immigr_men_data)
print(total_immigr_women_data)
print(total_emmigr_total_data)
print(total_emmigr_men_data)
print(total_emmigr_women_data)






# exit()

############ PREPARE  ############################
data = pd.DataFrame({'Immigrants % of total': [
                            total_immigr_men_data/total_immigr_total_data,
                            total_immigr_women_data/total_immigr_total_data,
                    ]},
                    index=[f'Men {round(100*total_immigr_men_data/total_immigr_total_data)}%', f'Women {round(100*total_immigr_women_data/total_immigr_total_data)}%'])
############ PLOT & SAVE #########################
data.plot(kind='pie', figsize=(7, 7), subplots=True)
plt.savefig(filepath + "__1-A.png")
plt.title("Immigrants by gender")
plt.show()
############ PREPARE  ############################
data = pd.DataFrame({'Emmigrants % of total': [
                            total_emmigr_men_data/total_emmigr_total_data,
                            total_emmigr_women_data/total_emmigr_total_data,
                    ]},
                    index=[f'Men {round(100*total_emmigr_men_data/total_emmigr_total_data)}%', f'Women {round(100*total_emmigr_women_data/total_emmigr_total_data)}%'])
############ PLOT & SAVE #########################
data.plot(kind='pie', figsize=(7, 7), subplots=True)
plt.savefig(filepath + "__1-B.png")
plt.title("Emmigrants by gender")
plt.show()




