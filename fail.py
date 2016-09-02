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
        coeff = nCr(j - i, t)
        if t % 2:
            coeff *= -1
        ex = i + t + 1
        term = coeff * pow(x, t) / float(ex)
        s += term
        if debug:
            print "%d %+.3f %+.3f %+.3f %+.3f"%(t, coeff, ex, term, s)
    return s * pow(x, i + 1)

def intLat1(i, j, debug=False):
    # Setting x = 1 makes us more efficient and accurate
    # More efficient because skips the exponentiation step; 1^ex == 1
    # More accurate because uses rational fractions
    s = Fraction(0, 1)
    if debug:
        print "t coeff  ex     term   s"
    for t in xrange(j - i + 1):
        coeff = nCr(j - i, t)
        if t % 2:
            coeff *= -1
        ex = i + t + 1
        term = Fraction(coeff, ex)
        s += term
        if debug:
            print "%d %+.3f %+.3f %+.3f %+.3f"%(t, coeff, ex, term, s)
    return float(s)

def intL0to1(i, j, debug=False):
    if i * 2 < j: # few failures, flip round for speed
        return intLat1(j - i, j, debug)
    return intLat1(i, j, debug)

def CLR(x, i, j, integral, debug=False):
    if i * 2 < j: # few failures, flip round for speed
        return 1.0 - intL(1.0 - x, j - i, j, debug) / float(integral)
    return intL(x, i, j, debug) / float(integral)

def series_CLR(ser, i, j, debug=False):
    integral = intL0to1(i, j, debug)
    return [CLR(x, i, j, integral, debug) for x in ser]

def LR(x, i, j, integral, debug=False):
    return L(x, i, j, debug) / float(integral)

def series_LR(ser, i, j, debug=False):
    integral = intL0to1(i, j, debug)
    return [LR(x, i, j, integral, debug) for x in ser]
