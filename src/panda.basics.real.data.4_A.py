from bokeh.io import curdoc, show
from bokeh.palettes import Category20
from bokeh.models.glyphs import HBar
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid, Title
import numpy as np
import numpy as np  
import pandas as pd
from bokeh.layouts import gridplot
import matplotlib.pyplot as plt

from bokeh.io import output_file, show
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


total_immigr_total_data = df.loc[:, [
    f"{year}" for year in years]].iloc[2:3].astype('int32')

total_immigr_men_data = df.loc[:, [
     f"Unnamed: {n}" for n in range(2, 24, 6)]].iloc[2:3].astype('int32')

total_immigr_women_data = df.loc[:, [
     f"Unnamed: {n}" for n in range(3, 25, 6)]].iloc[2:3].astype('int32')

# total_emmigr_total_data = df.loc[:, [
#     f"Unnamed: {n}" for n in range(4,28,6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

# total_emmigr_men_data = df.loc[:, [
#     f"Unnamed: {n}" for n in range(5, 29, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

# total_emmigr_women_data = df.loc[:, [
#     f"Unnamed: {n}" for n in range(6, 30, 6)]].iloc[2:3].astype('int32').sum(axis=1).loc['Age Group Total']

# FIX - commas
# total_other_data = df.loc[:, [f"{year} Alte cauze/ motive" for year in years]].replace(r'[^0-9]', '') #.astype('int32').sum(axis=1).loc['Tara de emigrare-total']
# the column - Other motifs - doesnt load well cause it's malformed, but we will calculate itl below using substraction ;)

print(total_immigr_total_data)
print(total_immigr_men_data)
print(total_immigr_women_data)

############ PREPARE  ############################
############ PLOT & SAVE #########################
output_file(filepath + "__4-A.html")

men = total_immigr_men_data.values.tolist()[0]
source_m = ColumnDataSource(data=dict(years=years, men=men,))

women =[-x for x in total_immigr_women_data.values.tolist()[0]]
source_w = ColumnDataSource(
    data=dict(years=years, women=women,))
# "Immigrants Men / Women[2014-2017]
plot1 = Plot(
    title=None, plot_width=700, plot_height=600,
    min_border=0, toolbar_location=None)
    
glyph_m = HBar(y="years", right="men", left=1000,
               height=0.31, fill_color=Category20[10][0])
plot1.add_glyph(source_m, glyph_m)

glyph_w = HBar(y="years", left="women", right=-1000,
               height=0.31, fill_color=Category20[10][1])
plot1.add_glyph(source_w, glyph_w)

xaxis = LinearAxis()
plot1.add_layout(xaxis, 'below')
yaxis = LinearAxis()
plot1.add_layout(yaxis, 'left')
plot1.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
#plot1.add_layout(Grid(dimension=1, ticker=yaxis.ticker))




show(gridplot([[plot1]]))
