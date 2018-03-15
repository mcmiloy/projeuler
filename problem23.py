from sympy import divisors

temp = [i for i in range(28123) if sum(divisors(i)) > i]

temp2 = {i + j for i in range(28123) for j in range(28123) if i+j < 28123}

temp3 = {i for i in range(28123)} - temp2

res = sum(list(temp3))

print(res)