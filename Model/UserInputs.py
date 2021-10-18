from yahoo_fin import options
import pandas_datareader as web
import pandas as pd
from datetime import datetime


stock = input("enter a stock ticker: ")
maturity_date = input("enter a maturity date (ex. October 15, 2021): ")
option_type = input("enter a type of option (c/p): ")
contract_type = ''

pd.set_option('display.max_columns', None)
chain = options.get_options_chain(stock, maturity_date)

start = datetime(2021, 9, 1)
end = datetime.now()

df = web.DataReader(stock, 'yahoo', start, end)
