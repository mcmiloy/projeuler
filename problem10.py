import functools
from math import ceil,sqrt

class mymethods:
    def __init__(self, data):
        self.data = data
    
    def prod(self):
        """Input: list
           Return: int
           Like sum() but with *"""
        return functools.reduce(lambda a,b: a*b, self.data)
    
    def isprime(self):
        """Input: int
           Return: bool
           Checks if a number is prime"""
        if self.data == 2: return True
        else: return all(self.data%i for i in range(2,ceil(sqrt(self.data))+1))

    def make_primelist(self):
        """Input: int
           Return: list containing ints
           This method creates a list of the first self.data prime numbers"""
        primelist = [2]
        n=3
        while len(primelist) <= self.data:
            if all(n%i for i in primelist):
                primelist.append(n)
            n += 1
        return primelist

    def make_primelist_alt(self):
        """Input: int
           Return: list containing ints
           This method creates a list of all prime numbers smaller than self.data"""
        primelist = [2]
        n=3
        while n < self.data:
            if all(n%i for i in primelist):
                primelist.append(n)
            n += 1
        return primelist

if __name__ == '__main__':
    def run():
        primelist = [2]
        n=3
        while n < 10000:
            if all(n%i for i in primelist):
                primelist.append(n)
            n += 1

        print(len(primelist))
        return sum(primelist)

    print(run())