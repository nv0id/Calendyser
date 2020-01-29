#!/usr/local/bin/python3
## Some SQL Tests ##

# https://www.youtube.com/watch?v=dUtBqDqmyQg

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

from math import pi
import random as rand

import pandas as pd
import sqlite3

import datetime

output_file("pie.html")

db = sqlite3.connect('/Users/nvoidmac/Desktop/events.db')


# Calendar='Work' OR Calendar='Undefined' OR Calendar='Travel' OR Calendar='Travel' OR Calendar='Personal'
res = (pd.read_sql_query("""SELECT EventName,sum(Duration) FROM allevents
WHERE AllDayEvent=0
AND
Calendar='Work'
GROUP BY EventName
""",db))
x = dict((i,j) for i,j in zip(res['EventName'],res['sum(Duration)']) if j>10)
print (x)
db.close()



data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]



p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
