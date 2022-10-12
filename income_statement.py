#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy as np
import pandas as pd
import pandas
import FundamentalAnalysis as fa
import sys
import configuration
# api_key = "bf8f4be551d1fdaafa51016aeb87462d"
# api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
# api_key = "7f03d4c7f7a1e60b7653a93d720381bb"
# api_key = "7a0b02329345d35dd5f8a916a0f39161"
# api_key = "ac5549ea4c42002d4a63472d839f934b"


def income_statement_analysis(ticker):
    api_key = configuration.get_api_key() 
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
    data = {'Year':year, 'Earning_Yield':ey_list, 'ROA': roa_list}
    df = pd.DataFrame(data)  
    # Print the output.
    print(df)


def p_e_ratio_return_on_asset(ticker):
    print("ticker:", ticker)
    api_key = configuration.get_api_key()
    companies = fa.available_companies(api_key)
    profile = fa.profile(ticker, api_key)
    stock_price=profile.loc['price', 0]
    print("stock price: ", stock_price)
    #I/S 
    income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
    #print ("income_statement_annually", income_statement_annually)
    # net income and earning pershare
    try: 
        n_i_2017=income_statement_annually.loc['netIncome', '2017']
        eps_2017=income_statement_annually.loc['eps', '2017']
        n_i_2018=income_statement_annually.loc['netIncome', '2018']
        eps_2018=income_statement_annually.loc['eps', '2018']
        n_i_2019=income_statement_annually.loc['netIncome', '2019']
        eps_2019=income_statement_annually.loc['eps', '2019']
        n_i_2020=income_statement_annually.loc['netIncome', '2020']
        eps_2020=income_statement_annually.loc['eps', '2020']
        n_i_2021=income_statement_annually.loc['netIncome', '2021']
        eps_2021=income_statement_annually.loc['eps', '2021']
    except: 
        print("eps exception")
    #asset
    # Collect the Balance Sheet statements
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    #print ("balance_sheet_annually", balance_sheet_annually)

    #Return on Asset
    try:
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
        tt_asset_2021= balance_sheet_annually.loc['totalAssets', '2021']
        ROA_2021 = n_i_2021/tt_asset_2021
         # print return on asset
        print("ROA_2017=n_i_2017/tt_asset_2017=", ROA_2017)
        print("ROA_2018=n_i_2018/tt_asset_2018=", ROA_2018)
        print("ROA_2019=n_i_2019/tt_asset_2019=", ROA_2019)
        print("ROA_2020=n_i_2020/tt_asset_2020=", ROA_2020)
    except:
        print("Return on asset exception")
    

   


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


def earning_yield(ticker):
    print("ticker:", ticker)
    api_key= configuration.get_api_key()
    companies = fa.available_companies(api_key)
    profile = fa.profile(ticker, api_key)
    stock_price=profile.loc['price', 0]
    print("stock price: ", stock_price)
    
    ey_2022 = 0
    ey_2021 = 0
    ey_2020 = 0
    #I/S 
    income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
    
    #earning pershare and earning yield
    try:         
        eps_2020=income_statement_annually.loc['eps', '2020']
        ey_2020 = eps_2020/stock_price
        print ("Earning yield 2020 = eps2020/current_stock_price=", ey_2020)
    except: 
        print("earning yield 2020 exception")
      
    try:  
        eps_2021=income_statement_annually.loc['eps', '2021']
        ey_2021 = eps_2021/stock_price
        print ("Earning yield 2021 = eps2021/current_stock_price=", ey_2021)
    except: 
        print("earning yield 2021 exception")
     
    try:  
        eps_2022=income_statement_annually.loc['eps', '2022']
        ey_2022 = eps_2022/stock_price
        print ("Earning yield 2022 = eps2012/current_stock_price=", ey_2022)
    except: 
        print("earning yield 2022 exception")
    

    # return on asset list
    #roa_list = [ROA_2017, ROA_2018, ROA_2019, ROA_2020]
   
   
    print("earning yield", [ey_2022, ey_2021, ey_2020])
    return [ey_2022, ey_2021, ey_2020]
      

if __name__ == "__main__":
    print("System Arguments: ")
    ticker = None
    if len(sys.argv) > 1: 
        ticker = sys.argv[1]           
    if ticker == None:
        ticker = "NRZ"
    print(str(sys.argv) + sys.argv[1])    
    print("ticker:", ticker)
    income_statement_analysis(ticker)





