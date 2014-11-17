#!/usr/bin/env python2

# Python 2 program that generates the fibonacci sequence
# to a user-specified length

import sys

def fib(n):
	f1, f2 = 0, 1
	k = 0
	while k < n:
		f3 = f1 + f2
		yield f1
		f1, f2 = f2, f3
		k += 1
	return

def main():
	try:
		n = int(sys.argv[1])
	except ValueError:
		print "Error: not a valid integer"
		sys.exit(1)
	l = []
	for d in fib(n):
		l.append(d)
	print l

if __name__ == '__main__':
	main()