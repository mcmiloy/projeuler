def run():
    primelist = [2]
    n=3
    while len(primelist) <= 10000:
        if all(n%i for i in primelist):
            primelist.append(n)
        n += 1

    return primelist[-1]

print(run())