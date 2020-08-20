import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

end = dt.datetime.now()
d = dt.timedelta(days = 365)
start = end - d
symbols = ['SPY', 'EFA', 'TLT', 'GLD']



dataframes = []
closes = []

for symbol in symbols:
    df = web.DataReader(symbol, 'yahoo', start, end)
    dataframes.append(df)
    closes.append(df['Adj Close'].round(decimals=2))

returns = []
print(closes)

for i in closes:
    ret = i[-1] / i[0] # return is last index / first index
    returns.append(ret)

# default first return as both max and min and assign correctly during loop
max = returns[0]
min = returns[0]
index = 0
best_performer = symbols[index]
worst_performer = symbols[index]

for i in returns:
    if max < i:
        max = i
        best_performer = symbols[index]
    if min > i:
        min = i
        worst_performer = symbols[index]
    index += 1

print('best performer,  ' + str(best_performer) + ': ' + str(max))
print('worst performer,  ' + str(worst_performer) + ': ' + str(min))
