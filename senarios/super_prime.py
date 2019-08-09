import math


def is_prime(number):
    for i in range(2 , int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def super_prime(n: int):
    if n < 10:
        return is_prime(n)



