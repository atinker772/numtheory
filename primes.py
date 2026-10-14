def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def gcd(a, b):
    """Greatest common divisor via the Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


print(is_prime(7))
print(is_prime(10))
print([n for n in range(30) if is_prime(n)])
print(gcd(48,18))
print(gcd(10928172, 192658))




