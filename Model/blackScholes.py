from Model.CleaningData import *
from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega, rho

bs_prices = []

class BlackScholes:

    @staticmethod
    def getBSPrice():

        for i in range(len(K)):
            prices = bs(option_type, S, K[i], T, r, sigma[i]).__round__(2)
            bs_prices.append(prices)

BlackScholes.getBSPrice()
