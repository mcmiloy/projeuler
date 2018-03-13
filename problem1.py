def run():
    """returns the sum of all multiples of 5 and 3 that are smaller or equal to 1000"""
    return sum(i for i in range(1000) if i%3 == 0 or i%5 == 0)

print(run())