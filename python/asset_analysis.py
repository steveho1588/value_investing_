#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy as np
import pandas as pd
import pandas
import FundamentalAnalysis as fa
import sys
# api_key = "bf8f4be551d1fdaafa51016aeb87462d"
# api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
# api_key = "7f03d4c7f7a1e60b7653a93d720381bb"
api_key = "7a0b02329345d35dd5f8a916a0f39161"

#companies = fa.available_companies(api_key)

def asset_analysis(ticker):

    profile = fa.profile(ticker, api_key)    
    # Show Key Metrics
    key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")  
    
    try:
        print("get current year metric")
        peRatioCurrentYear = key_metrics_annually.loc['peRatio', '2022']
        debtToAssetsCurrentYear = key_metrics_annually.loc['debtToAssets', '2022']
        returnOnCapitalEmployedCurrentYear = financial_ratios_annually.loc['returnOnCapitalEmployed', '2022']   
       
        print ("peRatio 2022", type(peRatioCurrentYear))
        print ("debtToAssets 2022 ", type(debtToAssetsCurrentYear))
        print ("returnOnCapitalEmployed 2022", type(returnOnCapitalEmployedCurrentYear))
        return [1/debtToAssetsCurrentYear, peRatioCurrentYear, returnOnCapitalEmployedCurrentYear]
    except:
        print("An exception occurred processing 2022")
    
    try:
        print("get Last Year metric")
        peRatioLastYear = key_metrics_annually.loc['peRatio', '2021']
        debtToAssetsLastYear = key_metrics_annually.loc['debtToAssets', '2021']
        returnOnCapitalEmployedLastYear = financial_ratios_annually.loc['returnOnCapitalEmployed', '2021']        
        print ("peRatio LastYear", type(peRatioLastYear))
        print ("debtToAssets LastYear ", type(debtToAssetsLastYear))
        print ("returnOnCapitalEmployed LastYear", type(returnOnCapitalEmployedLastYear))
        return [1/debtToAssetsLastYear, peRatioLastYear,returnOnCapitalEmployedLastYear]
    except:
        print("An exception occurred processing LastYear")
    
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
    