# -*- coding: utf-8 -*-
from bokeh.embed import components
from flask import Flask, render_template

# import plots
import P00104PYP000

script, div = components(P00104PYP000.plot)

app = Flask(__name__)

@app.route('/')
def bokeh():    
   return render_template('PN001.html', script=script, div=div)
