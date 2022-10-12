#Your API Key : bf8f4be551d1fdaafa51016aeb87462d
import numpy
import pandas as pd
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt
import sys
import numpy as np
from asset_analysis import *
from get_index_tickets_list import *

def main():
    # api_key = "bf8f4be551d1fdaafa51016aeb87462d"
    # api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
    # api_key = "7f03d4c7f7a1e60b7653a93d720381bb"
    api_key = "7a0b02329345d35dd5f8a916a0f39161"
    companies = fa.available_companies(api_key)
    print ("available companies", companies)
    print("System Arguments: ")
    ticker = None
    if len(sys.argv) > 1: 
        ticker = sys.argv[1]           
    if ticker == None:
        ticker = "NRZ"
    # print(str(sys.argv) + sys.argv[1])    
    print("ticker:", ticker)
    
    profile = fa.profile(ticker, api_key)
    stock_price=profile.loc['price', 0]
    print("stock price: ", stock_price)
    
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
    print("financial_ratios_annually", financial_ratios_annually)


# rank p/e: high 
# rank return on assets: high 
# rank asset/debt ratio: high

if __name__ == "__main__":
    
    #tickers = get_reits_tickers()
    tickers = get_equity_reits_tickers()
    # number_of_stock, len(tickers)
    volumn_size = 100 
    
    asset_metrics_df = pd.DataFrame({'Ticker':pd.Series([],dtype='string'),'assetToDebt':pd.Series([],dtype='float32'),'peRatio':pd.Series([],dtype='float32'),'returnOnCapitalEmployed':pd.Series([],dtype='float32')})
    print("asset_metrics_df columns types", asset_metrics_df.dtypes)
    for ticker in tickers[:volumn_size]:
        print("ticker:", ticker)
        asset_metrics = asset_analysis(ticker)
        print("asset_metrics", asset_metrics)
        # seperate ticker as string type and the other metric and float types,
        # otherwise it will mess up the datatype to object, which will mess up the rank() later on
        new_row_number = len(asset_metrics_df)
        asset_metrics_df.loc[new_row_number,'Ticker'] = ticker
        asset_metrics_df.loc[new_row_number,'assetToDebt':'returnOnCapitalEmployed'] = asset_metrics
    print("asset_metrics_df before add rank() \n", asset_metrics_df)
    print("asset_metrics_df columns type \n", asset_metrics_df.dtypes)    
    # add rank() function for each column
    asset_metrics_df['assetToDebt_Rank'] =  asset_metrics_df['assetToDebt'].rank()
    asset_metrics_df['peRatio_Rank'] =  asset_metrics_df['peRatio'].rank()
    asset_metrics_df['returnOnCapitalEmployed_Rank'] =  asset_metrics_df['returnOnCapitalEmployed'].rank()
#    asset_metrics_df['total_Rank'] =  asset_metrics_df['assetToDebt_Rank']*0.4 + asset_metrics_df['peRatio_Rank']*0.4 + asset_metrics_df['returnOnCapitalEmployed_Rank']*0.2
    asset_metrics_df['total_Rank'] =  (asset_metrics_df['assetToDebt_Rank']*0.4) * (asset_metrics_df['peRatio_Rank']*0.4) * (asset_metrics_df['returnOnCapitalEmployed_Rank']*0.2)
    
    asset_metrics_df = asset_metrics_df.sort_values(by=['total_Rank'], ascending=False)   
    print("asset_metrics_df after add rank() \n", asset_metrics_df)
    print("asset_metrics_df columns types \n", asset_metrics_df.dtypes)
    asset_metrics_df.to_csv("data/reits_sorted_by_total_rank.csv")
    
   
    


# array test code

# x = [1]
# y = [1, 2, 3]
# res = np.append(x, y)
# print("\nResult after appending x and y: ", res) 


# assign df columns dtype test code
# df = pd.DataFrame({'a':pd.Series([],dtype='int32'),'b':pd.Series([],dtype='float32')}) 

# old code that did not store the dtypes of columns, that lead to the rank() disfunction
# asset_metrics_df = pd.DataFrame(columns=['Ticker','assetToDebt', 'peRatio', 'returnOnCapitalEmployed'])    
# asset_metrics = np.append([ticker], asset_metrics)
# print("asset_metrics", asset_metrics)
# asset_metrics_df.loc[len(asset_metrics_df)] = asset_metrics

#test dataframe
# test_df = asset_metrics_df[["Ticker", "peRatio"]]
# test_df['peRatio_Rank'] =  test_df['peRatio'].rank()
# test_df = test_df.sort_values(by=['peRatio'], ascending=False)
# print("test df columns types", test_df.dtypes)