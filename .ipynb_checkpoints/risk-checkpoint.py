import numpy as np
from scipy import stats
import pandas as pd

def drawdown(returns, investment=1):
    wealth_index = investment * (1+returns).cumprod()
    prev_peaks = wealth_index.cummax()
    return (wealth_index - prev_peaks) / prev_peaks

def semideviation( returns):
    return returns[returns<0].std()

def var_historic( returns, level=5):
    returns = returns[~np.isnan(returns)]
    var = np.percentile(returns, 5, axis=0)
    return -1 * var

def var_gaussian( returns, level=5):
    '''
    Assume Gaussian model
    '''
    z = stats.norm.ppf(level / 100)
    var = -1 * (returns.mean() + z * returns.std()) 
    return var

def var_cornish_fisher( returns, level=5):
    '''
    Adjust z-score by curtosis and skewness since the distribution may not be gaussian
    '''
    z = stats.norm.ppf(level / 100)
    s = stats.skew(returns)
    k = stats.kurtosis(returns)
    z = (z +(z**2 - 1)*s/6 +(z**3 -3*z)*(k-3)/24 - (2*z**3 - 5*z)*(s**2)/36)
    var = -1 * (returns.mean() + z * returns.std()) 
    return var

def cvar_historic( returns, level=5):
    '''
    if the worst <level>% worst possible cases happen, then the expected shortfall of this scenario is the result of 
    this function
    '''
    worst = returns[returns < -1*self.var_historic(returns)]
    expected_shortfall = -1*worst.mean()
    return expected_shortfall


def var_summary(returns):
    var_hist = returns.aggregate(var_historic)
    var_gauss=returns.aggregate(var_gaussian)
    var_corfisher =returns.aggregate(var_cornish_fisher)
    vars = pd.concat([var_hist,var_gauss,var_corfisher], axis=1)
    vars.columns = ["historical", "gaussian", "corfish"]
    return vars


