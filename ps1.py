# Problem Set 1
# Name: Jafar Bakhshaliyev

# Problem 1

import math


def isPrime(n):
    """
    This function takes an integer number n and returns True if the number is prime number,
    otherwise it returns False
    :param n: int
    :return: boolean
    """
    check_prime = True
    if n == 1: check_prime = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: check_prime = False

    return check_prime


def nthPrime(nth):
    """
    This function takes an integer nth and return the nth prime number.
    :param nth: int
    :return: int
    """
    count = 0
    i = 2
    while count != nth:
        if isPrime(i): count += 1
        i += 1
    return i - 1


print(nthPrime(1000))


# Problem 2

def sumPrime(n):
    """
    This function takes a number n and returns logarithmic sum of all primes till n, input n, and ratio of these values.
    :param n: int
    :return: tuple
    """
    total = 0
    for i in range(2, (n+1)):
        if isPrime(i): total += math.log(i)
    return total, n, total / n

trials = [100,1000,10000,100000, 1000000]

for t in trials:
    print(sumPrime(t))