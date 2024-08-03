
import math 


# Future value of money
# Given you invest pval today at a certain rate r
# what is the future value of that in n periods
# if pmt is zero no regular payments
def fval(pval, r, n=1, pmt=0):
    if pmt != 0:
        return sum([ pmt * (1 + r)**i for i in range(0, n) ])
    else:
        return pval * (1 + r)**n


# Present value of a future sum
# What is the value of the present fval if you would 
# have invested it at a certain rate r for n periods
#
# In other words how much I need to invest today in order 
# to get fval in n periods at interest rate r
def pval(fv, r, n=1, pmt=0):
    if pmt != 0:
        return sum([ pmt / (1 + r)**i for i in range(1, n+1) ])
    else:
        return fv/(1 + r)**n



# Given a future value fv value of money
# what is the monthly payment given yearly interest r and n periods
def pmt(r, n=1, fv=0, pv=0):
    if pv == 0:
        return fv / sum([ (1 + r)**i for i in range(0, n) ]) 
    elif fv == 0:
        return pv / sum([ 1/(1 + r)**i for i in range(1, n+1) ]) 



# Given start capital of P, what is the
# fixed yearly interest rate given the aim is to
# achive F 
def interest_rate(P, F, n):
    return  (F / P)**(1/n) - 1

# Given start capital of P and the goal to accumulate F 
# at fixed yearly interest r, how many years would it take
# to achive the goal
def duration(P, F, r):
    return  math.log(F / P) / math.log(1+r)


# Return yearly balance given a fixed yearly `regular_payment`
# at `interest rate` for a period of `n` years.
# initial_payment is the initial account balance
# m = mth part of the year (m=1 is yearly interest yield, m=1/4)
#
# e.g what is the balance if I pay 750€ on my account every 3 month 
# for 10 years at the interest rate of 5%. 
# `compound_fixed(0, 750, 0.05, 4*10, m=4)[-1]`
def compound_fixed(initial_payment, regular_payment, interest_rate, n,m=1):
    balance = [initial_payment]
    for i in range(1,n+1):
        fv = (regular_payment + balance[i-1]) * (1+interest_rate)**(1/m)
        balance.append(fv)
    return balance[1:]
    

def ear(yearly_interest, rate):
    return (yearly_interest / rate)**rate