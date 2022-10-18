import math

primesList = [2]
bigPrime = 0
cur = 2
numRange = 10000000

printInterval = 10000
while cur< numRange:

    isPrime = True

    for prime in primesList:
        if cur % prime == 0:
            isPrime = False
        if prime > math.sqrt(cur):
            break

    if isPrime:
        primesList.append(cur)
        #print (cur)
        bigPrime = cur
    cur += 1

    if cur % printInterval == 0:
        print (f"The largest prime number under {cur} is {bigPrime}")

