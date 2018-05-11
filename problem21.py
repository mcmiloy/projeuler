from sympy import divisors

def divisor_sum(n):
    return sum(divisors(n)[:-1])

reslist = [(n1,n2) for n1 in range(1,300) for n2 in range(100,301) 
            and n1 == divisor_sum(n2)
            and n2 == divisor_sum(n1)]

print(reslist)