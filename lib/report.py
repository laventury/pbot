# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:53:22 2018

@author: wu3y
"""
import re 
from datetime import datetime
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, show

  
    
def PlotLine(DataIn):
       
    Pattern = re.compile("\('(?P<dt>.{7})',\s*(?P<ma>\d*),\s*(?P<mn>\d*),\s*(?P<mc>\d*)")
    
    DataPlot = Pattern.findall(str(DataIn))
    
    DateList = [datetime.strptime(d[0],'%Y-%m') for d in DataPlot]
    ValuesMA = [d[1] for d in DataPlot]
    ValuesMN = [d[2] for d in DataPlot]
    ValuesMC = [d[3] for d in DataPlot]
    
    p = figure(plot_width=800, plot_height=400)
    
    p.line(DateList, ValuesMA,line_width=2,line_color="red")
    p.circle(DateList, ValuesMA, legend="Medidas Passivo", fill_color="white", size=8)
    
    p.line(DateList, ValuesMN,line_width=2,line_color="green")
    p.circle(DateList, ValuesMN, legend="Medidas novas", fill_color="white", size=8)
    
    p.line(DateList, ValuesMC,line_width=2)
    p.circle(DateList, ValuesMC, legend="Medidas Concluída", fill_color="white", size=8)
    
    p.xaxis.formatter=DatetimeTickFormatter(
            hours=["%m/%Y"],
            days=["%m/%Y"],
            months=["%m/%Y"],
            years=["%m/%Y"],
        )
    
    show(p)