from numtheory import prime_factorization



def test_factorization():
    assert prime_factorization(360) == {2: 3, 3: 2, 5: 1}
    assert prime_factorization(97) == {97: 1}
