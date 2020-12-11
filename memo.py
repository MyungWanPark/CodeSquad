one_side = [['R','R','W'],['G','C','W'],['G','B','B']]

row1 = one_side[0]
row2 = one_side[1]
row3 = one_side[2]

# col1 = [one_side[0][0]] + [one_side[1][0]] + [one_side[2][0]]
# col2 = [one_side[0][1]] + [one_side[1][1]] + [one_side[2][1]]
# col3 = [one_side[0][2]] + [one_side[1][2]] + [one_side[2][2]]

col1 = []
col2 = []
col3 = []

for i in range(3):
    col1 += [one_side[i][0]]
    col2 += [one_side[i][1]]
    col3 += [one_side[i][2]]

print("row1 = ",row1)
print("row2 = ",row2)
print("row3 = ",row3)

print("col1 = ",col1)
print("col2 = ",col2)
print("col3 = ",col3)

