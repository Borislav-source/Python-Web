
from collections import deque
from math import sqrt


def check_if_number_is_prime(n):
    if 0 != n != 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def get_primes(sequence):
    sequence = deque(sequence)
    while sequence:
        number = sequence.popleft()
        if check_if_number_is_prime(int(number)):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
