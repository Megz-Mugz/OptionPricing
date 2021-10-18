import pandas as pd
from Model.CleaningData import *
from Model.blackScholes import *

data = []
labels = ['Strike', "Value Type", "Current Price", "BS Price"]

class NewDataFrame:

    @staticmethod
    def customDataFrame():
        for x in range(len(K)):
            row = (K[x], value_type[x], current_prices[x], bs_prices[x])
            data.append(row)

        df = pd.DataFrame.from_records(data, columns=labels).set_index('Strike')
        pd.set_option('max_rows', None)
        print(df)