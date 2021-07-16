import numpy as np


def payoffCall(S, E):
    return (abs(S - E) + S - E)/2


def payoffPut(S, E):
    return (abs(E - S) + E - S)/2




#--------------------------------------------------------
#               Option Strategies
#--------------------------------------------------------


# Payoff function for Bull Spread
# Buy one call option with a strike E1 and write another with a strike E2
# with the same expiration date
# If S > E2, then you can buy at E1 and sell at E2
def bullSpread(S, E1, E2):
    return payoffCall(S,E1)-payoffCall(S,E2)

# Payoff function for Bear Spread
# Write a put option with strike E1 and buy a put with strike E2
def bearSpread(S, E1, E2):
    return payoffCall(S,E1)-payoffCall(S,E2)

# The straddle consists of a call and a put with the same strike
def straddle(S, E):
    return payoffCall(S,E)+payoffPut(S,E)

# The strangle consists of a call and a put with a different strike
# EC = strike for call option
# EP = strike for put option
def strangle(S, EC, EP):
    return payoffCall(S,EC)+payoffPut(S,EP)
    