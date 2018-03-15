def sum_digits_modified(n):
    if n//10 == 0:
        return n**5
    else:
        return (n%10)**5 + sum_digits_modified(n//10)

temp = [i for i in range(2,1000000) if sum_digits_modified(i) == i]

print(temp)
print(sum(temp))