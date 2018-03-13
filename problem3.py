from math import sqrt, ceil
def run():
    factorlist = [i for i in range(2,ceil(sqrt(600851475143))) if 600851475143%i == 0 and isprime(i)]
    return factorlist[-1]


def isprime(n):
    if n == 2: return True
    else: return all(n%i for i in range(2,ceil(sqrt(n))+1))


if __name__ == '__main__':
    print(run())