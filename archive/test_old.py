#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy
import pandas as pd
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt
import sys
import numpy as np

def main():
    print("System Arguments: ")
    print(str(sys.argv))
    ticker = None
    if len(sys.argv) > 1: 
        ticker = sys.argv[1]           
    if ticker == None:
        ticker = "NRZ"
    print("ticker:", ticker)
    
    api_key = "bf8f4be551d1fdaafa51016aeb87462d"
    companies = fa.available_companies(api_key)
    profile = fa.profile(ticker, api_key)
    stock_price=profile.loc['price', 0]
    print("stock price: ", stock_price)
    #I/S 
    income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
    #print ("income_statement_annually", income_statement_annually)
    # net income and earning pershare
    n_i_2017=income_statement_annually.loc['netIncome', '2017']
    eps_2017=income_statement_annually.loc['eps', '2017']
    n_i_2018=income_statement_annually.loc['netIncome', '2018']
    eps_2018=income_statement_annually.loc['eps', '2018']
    n_i_2019=income_statement_annually.loc['netIncome', '2019']
    eps_2019=income_statement_annually.loc['eps', '2019']
    n_i_2020=income_statement_annually.loc['netIncome', '2020']
    eps_2020=income_statement_annually.loc['eps', '2020']    
    print("Net_income in Million 2017: "+ "${0:.2f} Million".format(n_i_2017/1000000) + ", 2018: "+ "${0:.2f} Million".format(n_i_2018/1000000) + ", 2019: "+ "${0:.2f} Million".format(n_i_2019/1000000)+ ", 2020: "+ "${0:.2f} Million".format(n_i_2020/1000000))
    
    


if __name__ == "__main__":
    main()






# saving to csv file
# balance_sheet_annually.to_csv("balance_sheet_annually.csv")
# income_statement_annually.to_csv("income_statement_annually.csv")





# #test print on console 
# print("type of income_statement_annually ", type(income_statement_annually))
# dataframe
# balance_sheet_annually.head()
# >>> balance_sheet_annually.head()
                                       # 2020                 2019  ...        1986        1985
# reportedCurrency                        USD                  USD  ...         USD         USD
# fillingDate                      2020-10-30           2019-10-31  ...  1986-09-30  1985-09-30
# acceptedDate            2020-10-29 18:06:25  2019-10-30 18:12:36  ...  1986-09-30  1985-09-30
# period                                   FY                   FY  ...          FY          FY
# cashAndCashEquivalents          38016000000          48844000000  ...   576200000   337000000

# balance_sheet_annually.shape
# balance_sheet_annually.to_csv("balance_sheet_annually.csv")
# income_statement_annually.to_csv("income_statement_annually.csv")