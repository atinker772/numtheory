def gcd(a, b):
    """Greatest common divisor via the Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

print(gcd(48,18))
print(gcd(10928172, 192658))
