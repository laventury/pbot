# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:53:22 2018

@author: wu3y
"""

from datetime import datetime
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, show, save
from bokeh.palettes import Category20

class plot:
    
    def __init__(self, title=None, data=[], legends=[], width=800, height=400):
        self.title = title
        self.legends = legends
        self.width = width
        self.height = height
        self.xdt = False
        self.data = data
        self.frmDtIn = '%Y-%m'
        self.frmDtOut = '%m/%Y'

    @property
    def dt(self):
        self.xdt = True
        return self
    
    @property
    def dma(self):
        self.frmDtIn = '%Y-%m-%d'
        self.frmDtOut = '%d/%m/%Y'
        return self
    
    def execute(self):
     
        self.fig = figure(title=self.title, plot_width=self.width, plot_height=self.height)
        
        if self.xdt:
            Xaxis = [datetime.strptime(x,self.frmDtIn) for x in self.data[0]]
               
            self.fig.xaxis.formatter=DatetimeTickFormatter(
                    hours=[self.frmDtOut],
                    days=[self.frmDtOut],
                    months=[self.frmDtOut],
                    years=[self.frmDtOut],
                )
        else:
            Xaxis = self.data[0]
            
        
        QtdColY = len(self.data) - 1
        
        # Prenchimento de legendas 
        legends = ['' for y in range(0,QtdColY)]
        if self.legends:
            ColInd = 0
            QtdLegends = len(self.legends)
            for legend in self.legends:
                legends[ColInd] = legend
                ColInd += 1
                if ColInd == QtdLegends:
                    break
        
        if QtdColY < 3 : 
            QtdPal = 3
        else: 
            QtdPal = QtdColY
        
        Palette = Category20[QtdPal]
        ColInd = 0
        
        for Yaxis in self.data[1:]:
            self.fig.line(Xaxis, Yaxis, legend=legends[ColInd], line_width=2,line_color=Palette[ColInd])
            self.fig.circle(Xaxis, Yaxis, legend=legends[ColInd], fill_color=Palette[ColInd], size=8)
            ColInd += 1
     
    def show(self):
        self.execute()  
        show(self.fig)
        return self
    
    def save(self):
        self.execute()  
        save(self.fig)
        return self
    
class page:
    
    def __init__(self):
        self.plots = []
        
    def plot_add(self,**kwargs):
        plotnew = plot(kwargs)
        self.plots.append(plotnew)
        return plotnew