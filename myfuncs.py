import functools

def factorial(n): return 1 if n==0 else n*factorial(n-1)

def bin_coeff(n,k): return factorial(n)/factorial(k)*factorial(n-k)


def prod(a_list):
    """Input: list
        Return: int
        Like sum() but with *"""
    return functools.reduce(lambda a,b: a*b, a_list)

def sum_digits(n):
    if n//10 == 0:
        return n
    else:
        return n%10 + sum_digits(n//10)