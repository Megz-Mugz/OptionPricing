import datetime
from datetime import date
from Model.UserInputs import *
import numpy as np


# black scholes variables
r = 0.01
T = 0
S = df["Adj Close"][-1]
K = []
sigma = []
current_prices = []
open_interest = []
value_type = []


class CleaningData:

    @staticmethod
    def callOrPut():
        global contract_type
        if 'c' in option_type.lower():
            contract_type = chain['calls']
        else:
            contract_type = chain['puts']

    @staticmethod
    def gettingStrike():
        global K
        vector = np.vectorize(np.float)
        K = list(vector(contract_type[['Strike']].values))
        K = [float(x) for x in K]

    @staticmethod
    def gettingLastPrice():
        global current_prices
        vector = np.vectorize(np.float)
        current_prices = list(vector(contract_type[['Last Price']].values))
        current_prices = [float(x) for x in current_prices]

    @staticmethod
    def gettingSigma():
        "this is getting implied volatility"
        global sigma
        new_sig = []
        sigma = list(contract_type[['Implied Volatility']].values)

        for i in sigma:
            iv = float(i[-1][:-2]) / 100
            new_sig.append(iv)
        sigma = new_sig


    @staticmethod
    def gettingT():
        global T
        contract_name = str(contract_type[['Contract Name']].values[0][0])
        date_str = contract_name[len(stock):]
        year = 2000 + int(date_str[:2])
        month = int(date_str[2:4])
        day = int(date_str[4:6])

        today = datetime.today().date()
        expiry_date = date(year, month, day)
        diff = expiry_date - today
        T = diff.days / 365

    @staticmethod
    def getOpenInterest():
        global open_interest
        open_interest = list(contract_type['Open Interest'])

    @staticmethod
    def getValueType():
        for strike in K:
            if strike >= S:
                value_type.append("---Out---")
            else:
                value_type.append("***In***")

    @staticmethod
    def printers():
        print(f'Strike Prices: {K}\n',
              f'Implied Volatility: {sigma}\n',
              f'Value Type: {value_type}')


CleaningData.callOrPut()
CleaningData.gettingT()
CleaningData.gettingStrike()
CleaningData.gettingSigma()
CleaningData.gettingLastPrice()
CleaningData.getValueType()
