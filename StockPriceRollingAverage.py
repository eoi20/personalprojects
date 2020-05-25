import numpy as ns
import pandas as pd
import quandl
import plotly
import plotly.express as px
quandl.ApiConfig.api_key = 'xxxxxxx'
data1 = quandl.get('OPEC/ORB', start_date="2017-01-01", end_date="2018-01-01") #OPEC Crude Oil Price

m1 = data1.to_numpy()
v1 = data1.index.to_numpy(dtype = object)
fig1 = px.line(x=v1, y=m1, labels={'x':'Date', 'y':'Values'}) # override keyword names with labels
fig1.show()

#numpy - it is an array 
#panda - more about operations on the data, that could be read from a file - doing a bulk operation - call the operation

data2 = data1['Value'].rolling(50).mean()
m2 = data2.to_numpy()
v2 = data2.index.to_numpy(dtype = object)
fig2 = px.line(x=v2[49:], y=m2[49:], labels={'x':'Date', 'y':'Values'}) # override keyword names with labels
fig2.show()

data3 = data1['Value'].pct_change(1)
m3 = ns.asarray(data3)
v3 = data3.index.to_numpy(dtype = object)
fig3 = px.line(x=v3, y=m3, labels={'x':'Date', 'y':'Values'}) # override keyword names with labels
fig3.show()