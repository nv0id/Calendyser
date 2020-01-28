#!/usr/local/bin/python3
## Analysis using pandas and bokeh ##

from bokeh.plotting import figure
from bokeh.palettes import Category20C
from bokeh.io import output_file,show
from bokeh.transform import cumsum

import numpy as np
import pandas as pd

from math import pi
import datetime as dt
import sqlite3



def plotter():
    output_file('pie.html')

def getdata():
    c.execute("""SELECT * FROM allevents WHERE AllDayEvent='0' AND WHERE
    """)





def main():
    pass


if __name__ == "__main__":
  conn = sqlite3.connect('/Users/nvoidmac/Desktop/events.db')
  c = conn.cursor()



  conn.close()
