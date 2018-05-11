from sympy import divisors

def tuplecomarer(tuple1, tuple2):
    if tuple1[0] == tuple2[1] and tuple1[1] ==  tuple2[0]:
        return True
    else:
        return False
    

divisor_sum_list = [(i,sum(divisors(i))-i) for i in range(2,10000)]

divisor_sum_list = list(filter(lambda x: x[1]>1 and x[1]<10000, divisor_sum_list))

reslist = []
for tup1 in divisor_sum_list:
    for tup2 in divisor_sum_list: 
        if tup1 != tup2 and tuplecomarer(tup1,tup2):
            reslist.append(tup1)
            divisor_sum_list.remove(tup1)
            divisor_sum_list.remove(tup2)

print(sum(map(lambda x: x[0] + x[1],reslist)))
