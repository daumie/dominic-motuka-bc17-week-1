#### A DOCUMENTATION TO ANDELA BOOTCAMP EXERCISES
---
##### Asymptotic analysis to primeSieve.py
The time complexity of the steps in primeSieve()
For each prime number
*primes <= sqrt(n)*
We cross out at most *n/primes* so we get the operations
*n/2*+*n/3*+*n/5*+*...*


The sum of the reciprocals of the *primes* <= *n* equals asymptotically :
        ```O(log log n)```
