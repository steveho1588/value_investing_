import numpy
import pandas as pd
import FundamentalAnalysis as fa
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
 
dividend_file = "data/divident_reit_list_09_2022.xlsx" 
utilities_file = "data/utility_stocks.xlsx" 
financial_file = "data/financial_stocks.xlsx" 

def get_sp500_tickers():
    print("get sp500 ")
    URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tickers = pd.read_html(URL)[0]['Symbol'].tolist()
    # print("Tickers: ", tickers)
    return tickers

def get_dividend_reits_tickers():
    print("get reits ")
    reit_list =  pd.read_excel(dividend_file, sheet_name='Characteristics')
    print ("reit_list", reit_list)
    tickers = pd.read_excel(dividend_file, sheet_name='Characteristics')['Ticker'].tolist()
    # print("Tickers: ", tickers)
    return tickers
    
def get_equity_reits_tickers():
    print("get reits ")
    reit_list =  pd.read_csv("data/list_of_US_REITs.csv")
    print ("reit_list", reit_list)
    tickers =  pd.read_csv("data/list_of_US_REITs.csv")['Symbol'].tolist()
    # print("Tickers: ", tickers)
    return tickers

def get_financial_tickers():
    print("get reits ")
    reit_list =  pd.read_excel(financial_file, sheet_name='Characteristics')
    print ("reit_list", reit_list)
    tickers = pd.read_excel(financial_file, sheet_name='Characteristics')['Ticker'].tolist()
    # print("Tickers: ", tickers)
    return tickers

def get_utilities_tickers():
    print("get reits ")
    reit_list =  pd.read_excel(utilities_file, sheet_name='Characteristics')
    print ("reit_list", reit_list)
    tickers = pd.read_excel(utilities_file, sheet_name='Characteristics')['Ticker'].tolist()
    # print("Tickers: ", tickers)
    return tickers

def get_russel_2000_tickers():
    print("get reits ")
    reit_list =  pd.read_excel(financial_file, sheet_name='Characteristics')
    print ("reit_list", reit_list)
    tickers = pd.read_excel(financial_file, sheet_name='Characteristics')['Ticker'].tolist()
    # print("Tickers: ", tickers)
    return tickers

if __name__ == "__main__":
    print("Get index tickets unit test ") 
    tickers = get_financial_tickers()
    print(tickers[:50]) 


