# Coupon Rate:  annual interest rate paid on the issuer's borrowed money
# Par value (Face value):  the amount of money that bond issuers promise to repay bondholders at the maturity date of the bond
# Maturity Date: date when the principal is repaid
# Bond Value:  PV(coupons) + PV(par)
# The price of a bond can be above or below its par value for many reasons, including:
# 
# interest rate adjustments to the bond;
# whether a bond credit rating has changed;
# supply and demand;
# a change in the creditworthiness of a bond's issuer;
# whether the bond has been called or is likely to be (or not to be) called; or,
# a change in the prevailing market interest rates.

from tvm import *
import math
import scipy.optimize as optimize
import numpy_financial as npf
import datetime


def bond_price(face_value, rate, nper):
    return  npf.pv(rate=rate, nper=nper, fv=face_value, pmt=0) * -1


def bond_yield(par, coupon_rate, n):
    """
    Akkumulierte Auszahlungen für eine Anleihe ohne Berücksichtigung der Auf-/Abzinsung
    """
    coupon = coupon_rate * par
    return par + n * coupon
    


def bond_value(par, coupon_rate, ytm, n):
    """
    Wert bzw Preis einer Anleihe unter Berücksichtigung der Rendite 
    ytm und Kuponzinssatz `coupon_rate` 
    """
    coupon = coupon_rate * par
    coupon_overal = sum([ pval(coupon, ytm, i) for i in range(1,n+1) ])
    return pval(par, ytm, n) + coupon_overal


# def bond_ytm(price, par, periods, coupon_rate, ratio=1):
def bond_ytm(par, par_rate, coupon_rate, nper, next_yield_date=None, buy_date=None):
    """
    Rendite einer Anleihe ist gleich dem Zinssatz, mit dem alle zukünftigen Zahlungen
    abzinsen muss, damit deren Summe dem heutigen Kurswert der Anleihe gleicht    
    """

    interim_coupon = 0
    interim_coupon_debt = 0
    
    if next_yield_date is not None and buy_date is not None:
        duration =  next_yield_date - buy_date
        interim_coupon =  (365 - duration.days) / 365
        interim_coupon_debt  = interim_coupon * coupon_rate * par
    
    coupon = coupon_rate * par
    value = par_rate * par
    
    FUN = lambda i: coupon/(1+i)**(nper - interim_coupon) * \
                    ((1+i)**nper - 1)/i  +  \
                    par/(1+i)**(nper-interim_coupon) - value - interim_coupon_debt


    return  optimize.newton(FUN, 0.01)



#TODO
# Zero-Bonds:
# - bounds with coupon rate = 0, no coupon payments
# - a bond holder receive the face value of the bond at maturity and no other cash flows
# - the price of the bond should always be lower than the face value

# Floater
# Floater mit Floor und/oder Cap
# Callable Bonds
# Convertible Bonds