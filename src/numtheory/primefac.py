def prime_factorization(n: int) -> dict[int, int]:
    """Return {prime: exponent}. E.g. 360 -> {2: 3, 3: 2, 5: 1}."""
    if n < 2:
        raise ValueError("n must be >= 2")
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
