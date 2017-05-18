"""fizzbuzz test"""
def fizz_buzz(number_tested):
    """implements fizzbuzz algorithm:
		divisible by 3 -> Fizz
		divisible by 5 -> Buzz
		divisible by both 3&5 -> FizzBuzz
	"""

    if number_tested%3 == 0 and number_tested%5 == 0:
        return 'FizzBuzz'
    elif number_tested % 3 == 0:
        return 'Fizz'
    elif number_tested%5 == 0:
        return 'Buzz'
    else:
        return number_tested
#print(fizz_buzz(15))


