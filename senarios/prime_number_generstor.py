import math

def is_prime (num : int) :
    for i in range (2 , 1+ int( math.sqrt(num))):
        if num % i == 0:
            return False

    return True


def super_prime(input_number : int) :

    if input_number < 10:
        return is_prime(input_number)

    if super_prime(input_number//10):
        return is_prime(input_number)



res = [i for i in range(2, 10000) if super_prime(i)]
print(res)

