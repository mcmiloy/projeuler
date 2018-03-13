import operator

def run():
    fibos = [1,2]
    while fibos[-1] <= 4000000:
        fibos.append(fibos[-1] + fibos[-2])
    
    fibos = filter(lambda x: x%2 == 0,fibos)
    return sum(fibos)
    

print(run())
