import numpy as np
import pandas as pd
import quandl
import os



class Quandler:
    
    def __init__(self):
        quandl.ApiConfig.api_key = os.environ["QUANDL"]

    def read(self, stock, gte, lte, db='WIKI/PRICES', dropna=True):
        '''
        read stock market data from wiki/prices
        '''
        df = quandl.get_table(db, 
                        ticker = stock, 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': gte, 'lte': lte }, 
                        paginate=True)
                        
        new = df.set_index('date')
        df = new.pivot(columns='ticker', values="adj_close")
        df = df.dropna() if dropna else df
        return df
    
    
    def get_hfi_returns(self):
        hfi = pd.read_csv("data/edhec-hedgefundindices.csv",header=0, index_col=0, parse_dates=True)
        hfi = hfi/100
        hfi.index = hfi.index.to_period('M')
        return hfi
    
    
    def get_ind_returns(self):
        df = pd.read_csv("data/ind30_m_vw_rets.csv",header=0,index_col=0,parse_dates=True)/100
        df.index = pd.to_datetime(df.index, format="%Y%m").to_period("M")
        df.columns = df.columns.str.strip()
        return df


