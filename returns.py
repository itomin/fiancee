import numpy as np
from scipy import stats

    
def total_return(series):
    return (series + 1).prod() - 1

def annualized_volatility(series, n=252):
    return series.std() * np.sqrt(n)

def annualized_returns(series, n=252):
    return (series + 1).prod()**(n/len(series)) - 1

def sharpe_ratio(series, riskfree_rate=0.03, n=252):
    """
    The greater a portfolio's Sharpe ratio, the better its risk-adjusted-performance.
    If the analysis results in a negative Sharpe ratio, it either means the risk-free rate 
    is greater than the portfolio’s return, or the portfolio's return is expected to be negative.
    In either case, a negative Sharpe ratio does not convey any useful meaning.
    """
    return (annualized_returns(series,n) - riskfree_rate) / annualized_volatility(series,n)