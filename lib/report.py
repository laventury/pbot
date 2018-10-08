# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:53:22 2018

@author: wu3y
"""
import re 
from datetime import datetime
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, show

def PrintSel(DataIn):
    print(DataIn)
    return None
    
    
def PlotLine(FilePlt, DataIn):
    
    Data = str(DataIn)
    ScriptFile = open(FilePlt,"r").read()
    ScriptFile = re.sub('(#DataPlot#)', Data, ScriptFile)
    print(ScriptFile)
    exec(ScriptFile)
