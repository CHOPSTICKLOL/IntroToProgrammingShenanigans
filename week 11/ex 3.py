rows=int(input("how many rows do you want?:"))
cols=int(input("how many columns do you want?:"))
MAT = [[int(input(f"for position {i},{j} pls add your numero:")) for j in range(cols)] for i in range(rows)]
total_sum=0
for row in MAT:
    for element in row:
        total_sum+=element
print(f'the total sum is {total_sum}')
average= total_sum/(len(MAT)*len(MAT[0]))
print(f'the average sum is {average}')
print(f"the last row if the matrix is{MAT[-1]} ")
main_diagonal=[MAT[i][i] for i in range(len(MAT))]
print(f'the main diagonal is {main_diagonal}')
