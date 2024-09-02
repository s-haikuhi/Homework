# Lesson 12.
"""
Exercise 9: Print Prime Numbers Function
Write a function that prints all prime numbers up to a given limit.
"""


def is_prime(given_number: int) -> bool:
    isPrime = True
    i = 2

    if given_number <= 1:
        return False
    else:
        while i <= given_number / 2:
            if given_number % i == 0:
                isPrime = False
                break
            else:
                i += 1
        return isPrime


def print_all_primes(given_limit: int) -> list:
    prime_numbers = []
    for n in range(1, given_limit):
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers


print(print_all_primes(18))

# Output for the given n = 18: [2, 3, 5, 7, 11, 13, 17]
