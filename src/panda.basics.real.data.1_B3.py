from bokeh.io import export_png
from bokeh.io import export_svgs
import itertools
from bokeh.palettes import Category20
from bokeh.palettes import brewer
from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot, column
import numpy as np
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, Div
from bokeh.plotting import figure, output_file, show
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import os
import imgkit


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


output_file(filepath + "__1-B3.html")



# create a new plot with a datetime axis type
plots1 = []
plots2 = []

lo_percent = 0
hi_percent = 0




dates = np.array(nationality_top_10_by_year_data.columns, dtype=np.datetime64)
x = 0

for index, row in nationality_top_10_by_year_data.iterrows():
    # total for each year
    for year in row.index:
        total = nationality_top_10_by_year_data[year].sum()
        row[year] = row[year] * 100 / total

    hi_percent += max(row) 
    lo_percent += min(row) 
    
    
    p = figure(plot_width=320, plot_height=280, x_axis_type="datetime")
    p.y_range.end = 100
    p.line(dates,
           row,  alpha=0.7, legend=index, line_width=2,color="green")

    p.circle(dates, row, size=5)
    plots1.append(p) if x >= 5 else plots2.append(p)
    x += 1

hi_percent /= 10
lo_percent /= 10

g = gridplot([plots1,plots2])
show(column(
    Div(text="<h2>Immigration by top 10 nationalities<br/>in % relative to the total immigrants for EACH YEAR<br>period [1993-2018]</h2>"),
    Div(text=f"<h4 style='color:red'>interesting fact: the average lo/hi is {round(lo_percent)}..{round(hi_percent)}% </h4>"),
    g
))

export_png(g, filename=filepath + "__1-B3.png")

