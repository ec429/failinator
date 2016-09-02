#! /usr/bin/python

import failfast
import rocket
import sys

def compare(a, b, n = 500):
	left = 0
	right = 0
	for i in xrange(n):
		p = i / float(n)
		# P(b = p && a < p) == pdf(b) * cdf(a)
		left += failfast.CLR(p, a.failures, a.launches) * failfast.LR(p, b.failures, b.launches)
		# and the reverse
		right += failfast.LR(p, a.failures, a.launches) * failfast.CLR(p, b.failures, b.launches)
	left /= float(n)
	right /= float(n)
	return left, right

def get_rocket_by_name(name):
	if name in rocket.by_name:
		return rocket.by_name[name]
	print >>sys.stderr, "No such rocket family", name
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print >>sys.stderr, "Usage: compare <family> <other_family>"
		sys.exit(1)

	first = get_rocket_by_name(sys.argv[1])
	second = get_rocket_by_name(sys.argv[2])
	left, right = compare(first, second)
	print "%s better: %1.3f%%"%(first.name, left * 100.0)
	print "%s better: %1.3f%%"%(second.name, right * 100.0)
