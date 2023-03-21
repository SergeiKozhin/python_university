from divisor_master import *

def test_divisors():
    assert divisors(12) == [1, 2, 3, 4, 6, 12]

def test_max_prime_divisor():
    assert max_prime_divisor(12) == 4