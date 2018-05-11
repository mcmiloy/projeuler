number_of_days = (365*100 + 25)
number_of_days2 = number_of_days - 6
number_of_weeks = int(number_of_days2/7)



days_list = ['Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']

days_list2 = days_list*(number_of_weeks + 1)

hundred_year_list = (([31,28,31,30,31,30,31,31,30,31,30,31] * 3
                     + [31,29,31,30,31,30,31,31,30,31,30,31]) * 25)




first_of_month_indexlist = [0]
sum_of_days = 0

for n in hundred_year_list:
    sum_of_days += n
    first_of_month_indexlist.append(sum_of_days)


counter = 0
for n in first_of_month_indexlist:
    if days_list2[n] == 'Sunday': counter += 1

print(counter)

