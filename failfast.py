#! /usr/bin/python
# like fail but use scipy's Beta functions, it's faster than me

from scipy.stats import beta

def LR(p, i, j):
    return beta.pdf(p, i, j)

def CLR(x, i, j):
	return beta.cdf(x, i, j)

def series_CLR(ser, i, j):
    return [CLR(x, i, j) for x in ser]

def series_LR(ser, i, j):
    return [LR(x, i, j) for x in ser]
