from problem3 import isprime
from functools import reduce

def prod(a_list):
    return reduce(lambda a,b: a*b, a_list, 1)

if __name__ == '__main__':
    primelist1_to_20 = [i for i in range(2,20) if isprime(i)]

    p5list = primelist1_to_20 + [2,2,2,3]
    print(p5list)

    print(prod(p5list))