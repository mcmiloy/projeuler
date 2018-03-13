from problem5 import prod
def is_pyth_triple(a,b,c): return (a*a + b*b) == c*c

mygen = ((a,b,c) for a in range(1000) for b in range(a+1,1000) for c in range(b+1,1000)
                 if a+b+c == 1000 and is_pyth_triple(a,b,c))

temp_res = next(mygen)

print(prod(temp_res))
