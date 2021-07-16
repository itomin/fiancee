import numpy as np


mu = 0.001
sigma = 0.01
start_price = 5



def gbm(mu, sigma, start, size=100):
    ''''
    Geometric Brownian Motion
    The returns are normally distributed with a mean of `mu` and the standard deviation `sigma` 
    - mu:  Positive value denotes a bullish trend and a negative value denotes a bearish trend
    - sigma: Volatility of the returns and a higher value denotes a more erratic price
    - start: Start price
    - size: Number of observations
    '''
    
    returns = np.random.normal(loc=mu, scale=sigma, size=size)
    ts = start*(1+returns).cumprod()

    return ts