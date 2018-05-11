def num_to_digits(n):
    if n//10 == 0: return [n]
    else: return [n%10] + num_to_digits(n//10)

def digitcounter_quick(n):
    res = 0
    while n>9:
        n = n//10
        res += 1
    return res + 1


def f(a,b,c):
    if sorted(num_to_digits(a) + num_to_digits(b) + num_to_digits(c)) == list(range(1,10)):
        return True
    else:
        return False

if __name__ == '__main__':
    resset = {(n1,n2,n1*n2) for n1 in range(1,100) for n2 in range(1,3000) if n1 != n2
               and digitcounter_quick(n1) + digitcounter_quick(n2)
               + digitcounter_quick(n1*n2) == 9
               and f(n1,n2,n1*n2)}

    print(resset)

