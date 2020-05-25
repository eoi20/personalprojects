import quandl
import plotly
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import datetime 
from datetime import datetime
from datetime import timedelta
py.init_notebook_mode(connected=True)
quandl.ApiConfig.api_key = 'xxxxx'
def QuandlData(x):
    return quandl.get(x, start_date="2017-01-01", end_date="2018-01-01")
_equit_ = ['EOD/AAPL','EOD/VZ','EOD/MSFT']
_equitval_ = {}

for i in _equit_:
    _equitval_[i] = QuandlData(i)

fig4 = go.Figure()
for i in _equitval_:
    #print(_equitval_[i].index)
   # print(_equitval_[i]['Adj_Close'])
    #print(type(i))
    fig4.add_trace(go.Scatter(x=_equitval_[i].index,y=_equitval_[i]['Adj_Close'], name = i))


fig4.show()

def DailyPercentage(x):
    for i in x:
        return (((x)/((x)-1))-1)
fig5 = go.Figure()
for i in _equitval_:
    #print(_equitval_[i].index)
   # print(_equitval_[i]['Adj_Close'])
    #print(type(i))
    fig5.add_trace(go.Histogram(x=_equitval_[i].index,y=DailyPercentage(_equitval_[i]['Adj_Close']), name = i))
fig5.update_layout(barmode='stack')


fig5.show()
