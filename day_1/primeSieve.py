import math # we will use the builtin math module

def isPrime(num): #Returns true if num is a prime number otherwise False
	if num < 2: # All numbers less than 2 are not prime
		return False
		''' Inspect  if num is divisible by
		 any number up to the square root of num'''
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True

'''In Mathematics the sieve of Eratosthenes is an algorithm  used to algorithm 
for finding all prime numbers up to any given limit
'''
def primeSieve(n):
	if type(n) != int:
		return 'TypeError'
	elif n < 0:
		return 'ValueError'
	else:
		primes = [] # Initialize array to hold prime numbers
		for i in range(n):
			if isPrime(i):
				primes.append(i)
		return primes
print(primeSieve(0))
print(primeSieve(-100))
print(primeSieve('rtr'))
print(primeSieve(9))


# def primeSieve(n): # returns a list of all prime numbers with  n as sieve size 
 
#  	sieve = [True]* n
#  	sieve[0] = False # Any number less than 2 is not prime
#  	sieve[1] = False

#  	for i in range(2,int(math.sqrt(n))+1): # converts list indices from tuples to integers
#  		reference = i*2 #starts at the first multiple of i which is i*2

#  		while reference < n:
#  			sieve[reference]=False #set the reference index in the sieve list to False
#  			reference += i #increments to the next number multiple of i

#  		'''After the while is loop is through, the sieve list will contain
#  		True for each index that is a prime number '''

#  	primes = [] # Initialize array to hold prime numbers
#  	for i in range(n):
#  		if sieve[i] == True:
#  			primes.append(i)
#  	return primes
