#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy as np
import pandas as pd
import pandas
import FundamentalAnalysis as fa
import sys
# api_key = "bf8f4be551d1fdaafa51016aeb87462d"
api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
#companies = fa.available_companies(api_key)
    
def asset_debt_analysis(ticker): 
    profile = fa.profile(ticker, api_key)
    debt_per_asset_2021 = 0 
    debt_per_asset_2020 = 0 
    
    try:
        stock_price=profile.loc['price', 0]
        print("stock price: ", stock_price)
    except:
        print("no price found for ", ticker)
        
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    #print(balance_sheet_annually)
    
    try:
        total_asset_2020 = balance_sheet_annually.loc['totalAssets', '2020']
        total_debt_2020 = balance_sheet_annually.loc['totalDebt', '2020']
        # print ("total debt 2020", total_debt_2020)
        # print ("total_asset_2020 ", total_asset_2020)
        if total_debt_2020 != 0:
            debt_per_asset_2020 = total_debt_2020/total_asset_2020
            print ("Asset/dept ratio 2020: ", debt_per_asset_2020)
        else:
            print ("Total_debt_2020 is 0, asset/dept ratio 2020: N/A")
    except:
        print("An exception occurred, no data found for 2020")
        
    try:
        total_asset_2021 = balance_sheet_annually.loc['totalAssets', '2021']
        total_debt_2021 = balance_sheet_annually.loc['totalDebt', '2021']
        # print ("Total debt 2021", total_debt_2021)
        # print ("TabErrorotal_asset_2021 ", total_asset_2021)
        if total_debt_2021 != 0:
            debt_per_asset_2021 = total_debt_2021/total_asset_2021
            print ("Debt/Asset ratio 2021: ", debt_per_asset_2021)
        else:
            print ("Total_debt_2021 is 0, Debt/Asset ratio 2021: N/A")
    except:
        print("An exception occurred")
    
    if debt_per_asset_2021 != 0:
        return debt_per_asset_2021
    else: 
        return debt_per_asset_2020
    

def balance_sheet_analysis(ticker): 
    profile = fa.profile(ticker, api_key)
    try:
        stock_price=profile.loc['price', 0]
        print("stock price: ", stock_price)
    except:
        print("no price found for ", ticker)
        
    # balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    # print(balance_sheet_annually)
    # balance_sheet_annually.to_csv(ticker + "_balance_sheet_annually.csv")
 
def asset_analysis(ticker):

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
    print("balance sheet unit test: ")
    ticker = None
    if len(sys.argv) > 1: 
        ticker = sys.argv[1]           
    if ticker == None:
        ticker = "NRZ"
    print(str(sys.argv) + sys.argv[1])    
    print("ticker:", ticker)
    print(asset_analysis(ticker))
    