res = sum(n1*n2 for n1 in range(1,101) for n2 in range(1,101) if n1 != n2)

if __name__ == '__main__':
    print(res)