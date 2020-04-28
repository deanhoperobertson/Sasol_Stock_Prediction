import numpy as np
import pandas as pd
from pandas_datareader import data as wb

def downloader():

	data=wb.DataReader("SSL", data_source = 'yahoo', start = '2010-1-1')

	#closing price vs adj closing depending on the real life application. For day trading where you are wanting to trade
	# a cfd the closing price is best. The adjusted price would if you are holding the stock and dividends/splits play a
	#role in your end return
	data['movement %'] = (data["Close"]/data["Close"].shift(1)-1)*100

	data['Target'] = data['movement %'].apply(lambda x : "Up" if x >0 else "Down")
	#drop the first column
	data=data.iloc[1:]

	return data
