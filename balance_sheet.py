#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy as np
import pandas as pd
import pandas
import FundamentalAnalysis as fa
import sys
from get_index_tickets_list import *
import configuration

# api_key = "bf8f4be551d1fdaafa51016aeb87462d"
# api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
# api_key = "7f03d4c7f7a1e60b7653a93d720381bb"
# api_key = "7a0b02329345d35dd5f8a916a0f39161"
# api_key = "ac5549ea4c42002d4a63472d839f934b"
 
# Original function 
# def asset_debt_analysis(ticker): 
    # asset_per_debt_2022 = 0
    # asset_per_debt_2021 = 0 
    # asset_per_debt_2020 = 0 
        
    # balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    # #print(balance_sheet_annually)
    
    # try:
        # total_asset_2020 = balance_sheet_annually.loc['totalAssets', '2020']
        # total_debt_2020 = balance_sheet_annually.loc['totalDebt', '2020']
        # # print ("total debt 2020", total_debt_2020)
        # # print ("total_asset_2020 ", total_asset_2020)
        # if total_debt_2020 != 0:
            # asset_per_debt_2020 = total_asset_2020/total_debt_2020
            # print ("Asset/dept ratio 2020: ", asset_per_debt_2020)
        # else:
            # print ("Total_debt_2020 is 0, asset/dept ratio 2020: N/A")
    # except:
        # print("An exception occurred, no data found for 2020")
        
    # try:
        # total_asset_2021 = balance_sheet_annually.loc['totalAssets', '2021']
        # total_debt_2021 = balance_sheet_annually.loc['totalDebt', '2021']
        # # print ("Total debt 2021", total_debt_2021)
        # # print ("TabErrorotal_asset_2021 ", total_asset_2021)
        # if total_debt_2021 != 0:
            # asset_per_debt_2021 = total_asset_2021/total_debt_2021
            # print ("Asset/Debt ratio 2021: ", asset_per_debt_2021)
        # else:
            # print ("Total_debt_2021 is 0, Debt/Asset ratio 2021: N/A")
    # except:
        # print("An exception occurred, no data found for 2021")
    
    # try:
        # total_asset_2022 = balance_sheet_annually.loc['totalAssets', '2022']
        # total_debt_2022 = balance_sheet_annually.loc['totalDebt', '2022']
        # # print ("Total debt 2021", total_debt_2022)
        # # print ("TabErrorotal_asset_2022 ", total_asset_2022)
        # if total_debt_2022 != 0:
            # asset_per_debt_2022 = total_asset_2022/total_debt_2022
            # print ("Asset/Debt ratio 2022: ", asset_per_debt_2022)
        # else:
            # print ("Total_debt_2022 is 0, Debt/Asset ratio 2022: N/A")        
    # except:
        # print("An exception occurred, no data found for 2022")
    
    # if asset_per_debt_2022 != 0:
        # return asset_per_debt_2022
    # elif asset_per_debt_2021 != 0:
        # return asset_per_debt_2021
    # else: 
        # return asset_per_debt_2020
    
#totalLiabilities

def asset_debt_liabilities_analysis(ticker): 
    asset_per_debt_2022 = 0
    asset_per_debt_2021 = 0 
    asset_per_debt_2020 = 0 
    asset_per_liabilities_2020 = 0
    asset_per_liabilities_2021 = 0 
    asset_per_liabilities_2022 = 0 
    api_key = configuration.get_api_key()    
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    # print(balance_sheet_annually)
    
    try:
        total_asset_2020 = balance_sheet_annually.loc['totalAssets', '2020']
        total_debt_2020 = balance_sheet_annually.loc['totalDebt', '2020']
        total_Liabilities_2020 = balance_sheet_annually.loc['totalLiabilities', '2020']
        # print ("total debt 2020", total_debt_2020)
        # print ("total_asset_2020 ", total_asset_2020)
        if total_debt_2020 != 0 and total_Liabilities_2020!= 0:
            asset_per_debt_2020 = total_asset_2020/total_debt_2020
            asset_per_liabilities_2020 = total_asset_2020/total_Liabilities_2020
            print ("Asset/dept ratio 2020: ", asset_per_debt_2020, ", Asset/Liabilties ratio 2020: ", asset_per_liabilities_2020)
        else:
            print ("Total_debt_2020 is 0, asset/dept ratio 2020: N/A")
    except:
        print("An exception occurred, no data found for 2020")
        
    try:
        total_asset_2021 = balance_sheet_annually.loc['totalAssets', '2021']
        total_debt_2021 = balance_sheet_annually.loc['totalDebt', '2021']
        total_Liabilities_2021 = balance_sheet_annually.loc['totalLiabilities', '2021']
        # print ("Total debt 2021", total_debt_2021)
        # print ("TabErrorotal_asset_2021 ", total_asset_2021)
        if total_debt_2021 != 0 and total_Liabilities_2021!= 0:
            asset_per_debt_2021 = total_asset_2021/total_debt_2021
            asset_per_liabilities_2021 = total_asset_2021/total_Liabilities_2021
            print ("Asset/Debt ratio 2021: ", asset_per_debt_2021)
        else:
            print ("Total_debt_2021 is 0, Debt/Asset ratio 2021: N/A")
    except:
        print("An exception occurred, no data found for 2021")
    
    try:
        total_asset_2022 = balance_sheet_annually.loc['totalAssets', '2022']
        total_debt_2022 = balance_sheet_annually.loc['totalDebt', '2022']
        total_Liabilities_2022 = balance_sheet_annually.loc['totalLiabilities', '2022']
        # print ("Total debt 2021", total_debt_2022)
        # print ("TabErrorotal_asset_2022 ", total_asset_2022)
        if total_debt_2022 != 0 and total_Liabilities_2022!= 0:
            asset_per_debt_2022 = total_asset_2022/total_debt_2022
            asset_per_liabilities_2022 = total_asset_2020/total_Liabilities_2022
            print ("Asset/Debt ratio 2022: ", asset_per_debt_2022)
        else:
            print ("Total_debt_2022 is 0, Debt/Asset ratio 2022: N/A")        
    except:
        print("An exception occurred, no data found for 2022")
    
    return [asset_per_debt_2022, asset_per_liabilities_2022, asset_per_debt_2021, asset_per_liabilities_2021, asset_per_debt_2020, asset_per_liabilities_2020]


def balance_sheet_analysis(ticker): 
    api_key = configuration.get_api_key()
    profile = fa.profile(ticker, api_key)
    try:
        stock_price=profile.loc['price', 0]
        print("stock price: ", stock_price)
    except:
        print("no price found for ", ticker)
        
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    print(balance_sheet_annually)
    # balance_sheet_annually.to_csv(ticker + "_balance_sheet_annually.csv")
 
def asset_analysis(ticker):
    api_key = configuration.get_api_key()
    profile = fa.profile(ticker, api_key)    
    # Show Key Metrics
    key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")  
    
    try:
        print("get 2022 metric")
        peRatio2022 = key_metrics_annually.loc['peRatio', '2022']
        debtToAssets2022 = key_metrics_annually.loc['debtToAssets', '2022']
        returnOnCapitalEmployed2022 = financial_ratios_annually.loc['returnOnCapitalEmployed', '2022']        
        print ("peRatio 2022", peRatio2022)
        print ("debtToAssets 2022 ", debtToAssets2022)
        print ("returnOnCapitalEmployed 2022", returnOnCapitalEmployed2022)
        return [peRatio2022, debtToAssets2022, returnOnCapitalEmployed2022]
    except:
        print("An exception occurred processing 2022")
    
    try:
        print("get 2021 metric")
        peRatio2021 = key_metrics_annually.loc['peRatio', '2021']
        debtToAssets2021 = key_metrics_annually.loc['debtToAssets', '2021']
        returnOnCapitalEmployed2021 = financial_ratios_annually.loc['returnOnCapitalEmployed', '2021']        
        # print ("peRatio 2021", peRatio2021)
        # print ("debtToAssets 2021 ", debtToAssets2021)
        # print ("returnOnCapitalEmployed", returnOnCapitalEmployed2021)
        return [peRatio2021, debtToAssets2021, returnOnCapitalEmployed2021]
    except:
        print("An exception occurred processing 2021")
    
    return [None, None, None]

if __name__ == "__main__":
    print("balance sheet analysis ")
    
    volumn_size = 15
    # tickers = get_equity_reits_tickers()
    tickers = get_dividend_reits_tickers()
    asset_debt_metrics_df = pd.DataFrame({'Ticker':pd.Series([],dtype='string'),'assetToDebt_2022':pd.Series([],dtype='float32'),'assetToLiabilities_2022':pd.Series([],dtype='float32'), 'assetToDebt_2021':pd.Series([],dtype='float32'),'assetToLiabilities_2021':pd.Series([],dtype='float32'),'assetToDebt_2020':pd.Series([],dtype='float32'), 'assetToLiabilities_2020':pd.Series([],dtype='float32'),})
    print("asset_debt_metrics_df")
    print(asset_debt_metrics_df)
    for ticker in tickers[:volumn_size]:
        print("ticker:", ticker)
        asset_metrics = asset_debt_liabilities_analysis(ticker)
        new_row_number = len(asset_debt_metrics_df)
        asset_debt_metrics_df.loc[new_row_number,'Ticker'] = ticker
        asset_debt_metrics_df.loc[new_row_number,'assetToDebt_2022':'assetToLiabilities_2020'] = asset_metrics

    print("asset_debt_metrics_df")
    print(asset_debt_metrics_df)
    
    # get all year
    # asset_debt_metrics_df = asset_debt_metrics_df.sort_values(by=['assetToLiabilities_2021'], ascending=False)   
    # get year with data
    asset_debt_metrics_df = asset_debt_metrics_df[["Ticker", "assetToDebt_2021", "assetToLiabilities_2021", "assetToDebt_2020", "assetToLiabilities_2020"]].sort_values(by=['assetToLiabilities_2021'], ascending=False)   
    print("asset_metrics_df after sorted \n", asset_debt_metrics_df)
    # if assetToLiabilities_2021 > 1.6 keep. else delete
    
    

# if __name__ == "__main__":
    # print("balance sheet unit test ")
    # ticker = None
    # if len(sys.argv) > 1: 
        # ticker = sys.argv[1]           
    # if ticker == None:
        # ticker = "NRZ"
    # print(str(sys.argv) + sys.argv[1])    
    # print(asset_debt_analysis(ticker))
