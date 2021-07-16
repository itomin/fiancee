
# Future value of money
# Given you invest pval today at a certain rate r
# what is the future value of that in n periods
def fval(pval, r, n=1):
    return pval * (1 + r)**n


# Present value of a future sum
# What is the value of the present fval if you would 
# have invested it at a certain rate r for n periods
#
# In other words how much I need to invest today in order 
# to get fval in n periods at interest rate r
def pval(fval, r, n=1):
    return fval/(1 + r)**n

