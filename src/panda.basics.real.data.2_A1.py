from bokeh.io import export_png
from bokeh.transform import cumsum
from bokeh.plotting import figure
from bokeh.palettes import Category20c
from bokeh.io import output_file, show
from math import pi
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import os

# generate the year diapason
years = list(range(1993,2011))


filename = '2. Imigranti dupa tara de emigrare si scopul sosirii , 1993-2010.csv'
filepath = f"{os.getcwd()}/data/real/{filename}"

df = pd.read_csv(filepath + "_fixed.csv", index_col=0, sep=";",
                 skiprows=1,
                 )

# FIX: we replace not numeric values with 0 - int so calculations could be done
df = df.replace('-0',0).replace('-',0) 



total_total_data = df.loc[:, [
    f"{year} Total" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_work_data = df.loc[:, [
    f"{year} La munca" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_study_data = df.loc[:, [
    f"{year} La studii" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']

total_family_data = df.loc[:, [
    f"{year} Imigratie de familie" for year in years]].astype('int32').sum(axis=1).loc['Tara de emigrare-total']



############ PLOT & SAVE #########################
output_file(filepath + "__2-A1.html")

x = {
  f'Work {round(100*total_work_data/total_total_data)}%': round(100*total_work_data/total_total_data),
  f'Study {round(100*total_study_data/total_total_data)}%': round(100*total_study_data/total_total_data),
  f'Family {round(100*total_family_data/total_total_data)}%': round(100*total_family_data/total_total_data)
}

data = pd.Series(x).reset_index(name='value').rename(
    columns={'index': 'country'})

data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

p = figure(plot_height=350, title='Immigrants % of total [1993-2010]', toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)

export_png(p, filename=filepath + "__2-A1.png")
