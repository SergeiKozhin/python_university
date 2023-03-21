a = 12

# 1. проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return 'Число не простое'
    else:
        return 'Число простое'


# 2. выводит список всех делителей числа;

def divisors(a):
    return [i for i in range(1, a + 1) if a % i == 0 ]


# 3. выводит самый большой простой делитель числа

def max_prime_divisor(a):
    c = 0
    for x in divisors(a):
        for i in range(2, int(a ** 0.5 + 1)):
            if x % i == 0:
                continue
            else:
                c = x
    return c


# 4. функция выводит каноническое разложение числа на простые множители

def kanon(a):
    i = 2
    kanon_list = []
    while i * i <= a:
        while a % i == 0:
            kanon_list.append(i)
            a = a / i
        i = i + 1
    if a > 1:
        kanon_list.append(int(a))
    return ('*').join(map(str, kanon_list))


# 5. функция выводит самый большой делитель (не обязательно простой) числа.

def max_divisor(a):
    return divisors(a)[-1]

print(max_prime_divisor(a))
