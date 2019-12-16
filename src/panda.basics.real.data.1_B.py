import itertools
from bokeh.palettes import Category20
from bokeh.palettes import brewer
from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
import numpy as np
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
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
nationality_top_10_by_year_data = df.loc[:, colum_names].astype('int32').sort_values(colum_names, ascending=False).head(10)
# print(nationality_top_10_by_year_data)



############ PLOT & SAVE #########################


# legend = []



output_file(filepath + "__1-B.html")
# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=700, x_axis_type="datetime")

dates = np.array(nationality_top_10_by_year_data.columns, dtype=np.datetime64)

x = 0
for index, row in nationality_top_10_by_year_data.iterrows():
    p.line(dates,
           row,  alpha=0.7, legend=index, line_width=3, color=Category20[10][x])
    x+=1

show(p)
