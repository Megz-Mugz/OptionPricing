from yahoo_fin import options
import pandas as pd


stock = input("Enter stock ticker (ex. FB)")
maturity_date = input('enter maturity date (ex. October 11, 2021): ')
option_type = input("would you like a call or put? (c/p)")
contract_type = ''

pd.set_option('display.max_columns', None)
chain = options.get_options_chain(stock, maturity_date)