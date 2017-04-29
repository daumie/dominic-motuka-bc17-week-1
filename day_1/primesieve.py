"""Using Sieve of Eratosthenes algorithm to get prime numbers"""
from math import sqrt


def isprime(num):
    """Returns True if a number is prime , otherwise False"""
    if num < 2:  # All numbers less than 2 are not prime
        return False
        ''' Inspect  if num is divisible by
		 any number up to the square root of num'''
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primesieve(num):
    """Uses sieve if eratosthenes algorithm to find prime numbers"""
    if isinstance(num, str):
        return 'TypeError'
    elif num < 0:
        return 'ValueError'
    else:
        primes = []  # Initialize array to hold prime numbers
        for i in range(num):
            if isprime(i):
                primes.append(i)
        return primes

#Driver program
# if __name__ == '__main__':
#     print(primesieve(0))
#     print(primesieve(-100))
#     print(primesieve('rtr'))
#     print(primesieve(9))
