from numtheory import gcd

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(17, 5) == 1
