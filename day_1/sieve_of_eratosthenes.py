"""Finds prime numbers using sieve of eratosthenes"""

def sieve(num):
    """create a boolean array "prime[0...n]" and initialize all entries as True.
     A value in prime[i] will finally be false if i is not prime, else True"""

    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        # If prime[p] is not changed then it is a prime number
        if prime[p] is True:
            # update all multiples of p
            for i in range(p * 2, num + 1, p):
                prime[i] = False
            p + 1
        # print all prime numbers
        for p in range(2, num):
            if prime[p]:
                print(p)


# Driver program
# if __name__ == '__main__':
#     num = 30
#     print("The list of prime numbers below or equal to", end=" ")
#     print(num, end=" is: \n")
#     sieve(num)
