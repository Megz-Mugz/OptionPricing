import datetime
from datetime import date
from Model.UserInputs import *


# black scholes variables
r = 0
# S = last price of underlying
# K = get from data
# T = time to maturity / 365
# sigma = implied volatility as a raw percent (50.00%) then divide by 100
# cOp = current price of option

class CleaningData:

    @staticmethod
    def callOrPut():
        global contract_type
        if 'C' in option_type:
            contract_type = chain['calls']
        else:
            contract_type = chain['puts']


    @staticmethod
    def gettingT():
        global T
        contract_name = str(contract_type[['Contract Name']].values[0][0])
        date_str = contract_name[len(stock):]
        year = 2000 + int(date_str[:2])
        month = int(date_str[2:4])
        day = int(date_str[4:6])

        today = datetime.datetime.today().date()
        expiry_date = date(year, month, day)
        diff = expiry_date - today
        T = diff.days / 365
        print(T)

CleaningData.callOrPut()
print(contract_type)
CleaningData.gettingT()