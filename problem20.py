def factorial(n): return 1 if n == 0 else n*factorial(n-1)

f100 = factorial(100)

def sum_digits(n):
    if n//10 == 0:
        return n
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(f100))
