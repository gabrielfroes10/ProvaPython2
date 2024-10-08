def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes


array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = find_primes(array)
print("Números primos:", primos)
