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
total_by_nationality_data = df.loc[:, colum_names].astype('int32').sum(axis=1).sort_values(0,ascending=False).head(10)
print(total_by_nationality_data.index)


############ PLOT & SAVE #########################
output_file(filepath + "__1-A1.html")
data =total_by_nationality_data.reset_index(name='value')

print(data)    
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(data)]

p = figure(plot_height=350, title="Top 10 Immigrants by nationality [1993-2018]", toolbar_location=None,
           tools="hover", tooltips="@nationality: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='nationality', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)


export_png(p, filename=filepath + "__1-A1.png")
