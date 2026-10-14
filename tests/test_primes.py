from numtheory import is_prime, gcd

def test_small_primes():
    assert [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(17, 5) == 1
