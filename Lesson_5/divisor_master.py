a = [i for i in range(0, 1001)]


def prime_number(n):
    lst = []
    for i in a:
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

print(prime_number(a))