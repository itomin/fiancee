import numpy as np


def put(S, E, long=True):
    return payoff(S,E,call=False,long=long)

def call(S, E, long=True):
    return payoff(S,E,long=long)

def payoff(S, E, call=True, long=True):
    C = 1 if call else -1
    L = 1 if long else -1
    moneyness = (abs(C* S - C* E) + C * S - C * E)/2
    
    return L*moneyness

def profit(call, premium, buyer=True):
    return call - premium if buyer else premium - call


#--------------------------------------------------------
#               Option Strategies
#--------------------------------------------------------


# Payoff function for Bull Spread
# Buy one call option with a strike E1 and write another with a strike E2
# with the same expiration date
# If S > E2, then you can buy at E1 and sell at E2
def bullSpread(S, E1, E2):
    return payoff(S,E1)-payoff(S,E2)

# Payoff function for Bear Spread
# Write a put option with strike E1 and buy a put with strike E2
def bearSpread(S, E1, E2):
    return payoff(S,E1)-payoff(S,E2)

# The straddle consists of a call and a put with the same strike
def straddle(S, E):
    return payoff(S,E)+payoff(S,E,call=False)

# The strangle consists of a call and a put with a different strike
# EC = strike for call option
# EP = strike for put option
def strangle(S, EC, EP):
    return payoff(S,EC)+payoff(S,EP,call=False)
    