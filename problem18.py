l1 = [75]
l2 = [95, 64]
l3 = [17, 47, 82]
l4 = [18, 35, 87, 10]
l5 = [20, 4, 82, 47, 65]
l6 = [19, 1, 23, 75, 3, 34]
l7 = [88, 2, 77, 73, 7, 63, 67]
l8 = [99, 65, 4, 28, 6, 16, 70, 92]
l9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
l10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
l11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
l12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17,57]
l13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
l14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
l15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

list_of_lists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15]
left_steps = 0
right_steps = 0
reslist = [75]

for i in range(1,15):
    temp1 = sum(x[right_steps] for x in list_of_lists[i:])
    temp2 = sum(x[len(x) -1 - left_steps] for x in list_of_lists[i:])
    if temp1 > temp2:
        reslist.append(list_of_lists[i][right_steps])
        left_steps += 1
    else:
        reslist.append(list_of_lists[i][right_steps+1])
        right_steps += 1

print(sum(reslist))