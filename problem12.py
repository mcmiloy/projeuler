import itertools, math
from problem10 import mymethods
from problem5 import prod
from collections import Counter
from sympy import factorint

"""
go = mymethods(100000)
primelist = go.make_primelist_alt()
"""

"""
def prime_factorization(n):
    if n in primelist:
        return [n]
    else:
        for z in primelist:
            if n%z == 0: break
        return [z] + prime_factorization(n/z)
"""
"""
def prime_factorization(n):
    res = []
    while n not in primelist:
        for i in primelist:
            if n%i == 0: break
        res.append(i)
        n = n/i
    res.append(n)
    return res
"""


def count_divisors(n):
    count = [i+1 for i in factorint(n).values()]
    return prod(count)


def triangle_num(i): return sum(range(i))

triangle_num_gen = (triangle_num(i) for i in itertools.count(start = 2))

if __name__ == '__main__':
    for cou in triangle_num_gen:
        if count_divisors(cou) >= 500:
            break

    print(cou)


