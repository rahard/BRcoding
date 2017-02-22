import plotly.plotly as py
from plotly.graph_objs import *
# plotly.tools.set_credentials_file(username='rahard', api_key='cLTpRQtkzkpMBSFOYbR5')

print "hello"


trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.plot(data, filename = 'basic-line')
