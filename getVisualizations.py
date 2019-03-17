import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime
import requests


import fix_yahoo_finance as yf

yf.pdr_override()

data = pdr.get_data_yahoo("SPY", start="2018-09-12", end="2019-03-16")

#print(data)
#df.iloc[:, [True, False, True, False]]
print(data['Adj Close'][0])
