#!/usr/bin/env python2

# Python 2 program that generates pi to user-specified number of digits
# Uses BBP formula

import sys
from decimal import *

def pidigits(n):
	"""yields up to n digits of pi using BBP formula"""
	k = 0
	while k < n:
		yield ((Decimal(1)/(16**k))*((Decimal(4)/(8*k + 1)) - (Decimal(2)/(8*k + 4)) - (Decimal(1)/(8*k + 5)) - (Decimal(1)/(8*k + 6))))
		k +=1
	return

def main():
	try:
		n = int(sys.argv[1])
	except ValueError:
		print "Error: given argument not a valid integer"
		sys.exit(1)
		
	pi = Decimal(0)
	for d in pidigits(n):
		pi += d
	print str(pi)[:(2+n)]		
 
if __name__ == '__main__':
	main()        
