from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


# lst = get_n_primes(1_000_000)


class PrimeIterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


first_1_000_000_primes = PrimeIterator(1_000_000)

print(next(first_1_000_000_primes))
print(next(first_1_000_000_primes))
print(next(first_1_000_000_primes))


def prime_generator(n):
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1


gen = prime_generator(1_000_000)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
