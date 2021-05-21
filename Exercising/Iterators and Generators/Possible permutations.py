from itertools import permutations


def possible_permutations(sequence):
    for number in permutations(sequence):
        yield number

[print(n) for n in possible_permutations([1, 2, 3])]