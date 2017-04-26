#!/usr/bin/python
# -*- coding: utf-8 -*-

def SieveOfEratoshenes(n):
	'''create a boolean array "prime[0...n]" and initialize all entries as True.
	A value in prime[i] will finally be false if i is not prime, else True'''

	prime = [True for i in range(n+1)]
	p = 2
	while (p*p <= n):
		# If prime[p] is not changed then it is a prime number
		if(prime[p] == True):
			# update all multiples of p
			for i in range(p*2, n+1, p):
				prime[i] = False
			p+1
		# print all prime numbers
		for p in range(2, n):
			if prime[p]:
				print (p)
# Driver program
if __name__ == '__main__':
	n = 30 
	print("The list of prime numbers below or equal to", end= " ")
	print(n, end= " is: \n")
	SieveOfEratoshenes(n)



