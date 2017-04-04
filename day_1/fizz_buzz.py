def fizz_buzz(n): # Returns the argument it receives
	if n%3 == 0 and n%5 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n%5 == 0:
		return 'Buzz'
	else:
		return str(n)
#print(fizz_buzz(1000))


