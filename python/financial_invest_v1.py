#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy as np
import pandas as pd
import pandas
import FundamentalAnalysis as fa
import sys

def main():
    print("System Arguments: ")
    print(str(sys.argv))
    #ticker = "NRZ"
    ticker = sys.argv[1] 
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

    #asset
    # Collect the Balance Sheet statements
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    #print ("balance_sheet_annually", balance_sheet_annually)

    #Return on Asset
    #For ROA_2017
    tt_asset_2017= balance_sheet_annually.loc['totalAssets', '2017']
    ROA_2017 = n_i_2019/tt_asset_2017 
    #For ROA_2018
    tt_asset_2018= balance_sheet_annually.loc['totalAssets', '2018']
    ROA_2018 = n_i_2018/tt_asset_2018 
    #For ROA_2019
    tt_asset_2019= balance_sheet_annually.loc['totalAssets', '2019']
    ROA_2019 = n_i_2019/tt_asset_2019 
    #For ROA_2020
    tt_asset_2020= balance_sheet_annually.loc['totalAssets', '2020']
    ROA_2020 = n_i_2020/tt_asset_2020

    # print return on asset
    print("ROA_2017=n_i_2017/tt_asset_2017=", ROA_2017)
    print("ROA_2018=n_i_2018/tt_asset_2018=", ROA_2018)
    print("ROA_2019=n_i_2019/tt_asset_2019=", ROA_2019)
    print("ROA_2020=n_i_2020/tt_asset_2020=", ROA_2020)


    # Earning Yield
    ey_2017 = eps_2017/stock_price
    ey_2018 = eps_2018/stock_price
    ey_2019 = eps_2019/stock_price
    ey_2020 = eps_2020/stock_price
    # Print earning yield 
    print ("Earning yield 2017% = eps2017/current_stock_price=", ey_2017)
    print ("Earning yield 2018% = eps2018/current_stock_price=", ey_2018)
    print ("Earning yield 2019% = eps2019/current_stock_price=", ey_2019)
    print ("Earning yield 2020% = eps2019/current_stock_price=", ey_2020)

    year = np.arange(2017, 2021, 1);
    ey_list = [ey_2017, ey_2018, ey_2019, ey_2020]
    roa_list = [ROA_2017, ROA_2018, ROA_2019, ROA_2020]
    data = {'Year':year, 'Earning_Yield':ey_list, 'ROA': roa_list}
    df = pd.DataFrame(data)  
    # Print the output.
    print(df)

    # saving to csv file
    # balance_sheet_annually.to_csv("balance_sheet_annually.csv")
    # income_statement_annually.to_csv("income_statement_annually.csv")



if __name__ == "__main__":
    main()













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