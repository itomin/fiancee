import pytest
from tvm import *


def test_fval():
    # Suppose you want to pay $10,000 each year on your account
    # for 25 years at the interest rate of 8%, what is your 
    # bank account after 25 years
    assert pytest.approx(2590565) == fval(0, n=40, r = 0.08,pmt=10000) 


def test_pval():
    # How much money do you need to put
    # in the bank today so that you can 
    # spend $10,000 every year for the next 25 years,
    # starting at the end of this year? 
    # if r = 0 than you need 250000 on your bank account
    assert pytest.approx(140939, 1) == pval(0, n=25, r = 0.05,pmt=10000)



def test_pmt():
    # Suppose you want $500,000 when you retire 25 years from now.
    # How much must you invest each year, starting at the end of this year,
    # if the interest-rate is 8%
    assert pytest.approx(6839, 1) ==  pmt(n=25, r = 0.08, fv=500000)
    
    # Suppose you have a loan of $100,000, what is your yearly
    # payment, when you want to payoff the loan in 5 years at the interest
    # rate of 10%
    assert pytest.approx(26379, 1) == pmt(n=5, r = 0.1, pv=100000)