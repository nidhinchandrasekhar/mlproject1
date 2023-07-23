import pickle
from flask import flask,request,render_template
import numpy as np
import pandas as pd

application=flask(__name__)
app=application

#route for a home page
@app.route('/')
def index():
    return render