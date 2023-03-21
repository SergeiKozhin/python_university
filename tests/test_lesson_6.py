import divisor_master


def test_divisors():
    assert divisor_master.divisors(12) == [1, 2, 3, 4, 6, 12]


def test_max_prime_divisor():
    assert divisor_master.max_prime_divisor(12) == 4


def test_kanon():
    assert divisor_master.kanon(12) == '2*2*3'


def test_max_divisor():
    assert divisor_master.max_divisor(12) == 12


def test_is_prime():
    assert divisor_master.is_prime(12) == 'Число не простое'