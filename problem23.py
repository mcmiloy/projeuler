from sympy import divisors
import collec

temp = [i for i in range(15000) if sum(divisors(i)[:-1]) > i]



temp3 = {i for i in range(28123)} - temp2

res = sum(list(temp3))

print(res)