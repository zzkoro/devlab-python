def func_dn(n):
    return n + sum([int(ni) for ni in str(n)])

self_numbers = set(range(1,5000)) - set(func_dn(n) for n in range(1,5000))

print('sum of self numbers:', sum(self_numbers))

