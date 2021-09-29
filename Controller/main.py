import numpy as np
from scipy.stats import norm
import pandas_datareader as web
from datetime import datetime

start = datetime(2021, 9, 1)

df = web.DataReader('aapl', 'yahoo', start, datetime.now())

# define variables
r = 0 # interest rate
S = df["Adj Close"][-1]
K = float(input('enter strike price: ')) # strike
T = int(input('enter days till maturity: ')) / 365 # time to maturity
sigma = float(input('enter implied volatility (%): ')) / 100 #volatility
cOp = float(input("enter current option price: "))

def blackScholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for call/put"

    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*(np.sqrt(T)))
    d2 = d1 - sigma*(np.sqrt(T))
    try:
        if type == 'C':
            t_price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == 'P':
            t_price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return f'---------- Theoretical Value ----------\n' \
               f'Fair Price: {round(t_price, 2)}\n' \
               f'Percent from Current Price: {round(((t_price - cOp) / cOp)*100, 2)}%'

    except:
        print("Please Confirm all option parameters above!!!")


print(blackScholes(r, S, K, T, sigma, type='P'))