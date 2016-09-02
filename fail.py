#! /usr/bin/python

from operator import mul
from fractions import Fraction

def nCr(n, r):
    """n choose r"""
    # From http://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3027128#3027128
    return int(reduce(mul, (Fraction(n - i, i + 1) for i in xrange(r)), 1))

def L(p, i, j, debug=False):
    """i failures in j trials, normalised by jCi"""
    return pow(p, i) * pow(1 - p, j - i)

def intL(x, i, j, debug=False):
    # Expand the polynomial L, and integrate term-by-term
    # At x = 0 all terms are zero, so just evaluate at p = x
    s = 0
    if debug:
        print "t coeff  ex     term   s"
    for t in xrange(j - i + 1):
        # (-1)^t * (j - i choose t) * x^(j+1-t) / (j+1-t)
        coeff = nCr(j - i, t)
        if t % 2:
            coeff *= -1
        ex = i + t + 1
        term = coeff * pow(x, ex) / float(ex)
        s += term
        if debug:
            print "%d %+.3f %+.3f %+.3f %+.3f"%(t, coeff, ex, term, s)
    return s

def CLR(x, i, j, integral, debug=False):
    return intL(x, i, j, debug) / float(integral)

def series_CLR(ser, i, j, debug=False):
    integral = intL(1.0, i, j, debug)
    return [CLR(x, i, j, integral, debug) for x in ser]

def LR(x, i, j, integral, debug=False):
    return L(x, i, j, debug) / float(integral)

def series_LR(ser, i, j, debug=False):
    integral = intL(1.0, i, j, debug)
    return [LR(x, i, j, integral, debug) for x in ser]
