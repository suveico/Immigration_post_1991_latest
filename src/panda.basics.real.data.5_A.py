from bokeh.models import HoverTool
import itertools
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
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


# generate the year diapason
years = list(range(1960,2018))


filename = '5. World bank_POP.TOTL_DS2_en_excel_v2_566190.xls'
filepath = f"{os.getcwd()}/data/real/{filename}"

df = pd.read_excel(filepath, index_col=0, sep=";",
                 skiprows=3,
                 # quotechar="\""
                 ###, names=['nationality'] + colum_names
                 )['Moldova':'Moldova']


total_population = df.loc[:, [str(y) for y in years]].astype('int32')




############ PREPARE  ############################
############ PLOT & SAVE #########################


output_file(filepath + "__5-A.html")
# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=700, x_axis_type="datetime")

dates = np.array([str(y) for  y in years], dtype=np.datetime64)
population = total_population.values.tolist()[0]


# Basic plot setup
plot = figure(plot_width=1200, plot_height=700, x_axis_type="datetime", tools="",
              toolbar_location=None, title='Moldova\' population [1962-2018]')

plot.line(dates, population, line_dash="4 4", line_width=1, color='gray')

cr = plot.circle(dates, population, size=20,
                 fill_color="grey", hover_fill_color="firebrick",
                 fill_alpha=0.05, hover_alpha=0.3,
                 line_color=None, hover_line_color="white")

plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))

show(plot)


