#! /usr/bin/python

import failfast
import rocket
import sys

def compare(a, b, n=500, prior=0.5):
    left = 0
    right = 0
    for i in xrange(n):
        p = i / float(n)
        # P(b = p && a < p) == pdf(b) * cdf(a)
        left += failfast.CLR(p, a.failures + prior, a.launches + prior) * failfast.LR(p, b.failures + prior, b.launches + prior)
        # and the reverse
        right += failfast.LR(p, a.failures + prior, a.launches + prior) * failfast.CLR(p, b.failures + prior, b.launches + prior)
    left /= float(n)
    right /= float(n)
    return left, right

def get_rocket_by_name(name):
    if name in rocket.by_name:
        return rocket.by_name[name]
    print >>sys.stderr, "No such rocket family", name
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        first = get_rocket_by_name(sys.argv[1])
        for second in rocket.families:
            if second == first: continue
            left, right = compare(first, second)
            print "%s %1.3f%% vs %s %1.3f%%"%(first.name, left * 100.0, second.name, right * 100.0)
    elif len(sys.argv) == 3:
        first = get_rocket_by_name(sys.argv[1])
        second = get_rocket_by_name(sys.argv[2])
        left, right = compare(first, second)
        #print "%s better: %1.3f%%"%(first.name, left * 100.0)
        #print "%s better: %1.3f%%"%(second.name, right * 100.0)
        print "%s %1.3f%% vs %s %1.3f%%"%(first.name, left * 100.0, second.name, right * 100.0)
    else:
        print >>sys.stderr, "Usage: compare <family> [<other_family>]"
        sys.exit(1)
