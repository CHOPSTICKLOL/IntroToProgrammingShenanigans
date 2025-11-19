rows=int(input("how many rows do you want?:"))
cols=int(input("how many columns do you want?:"))
MAT = [[int(input(f"for position {i},{j} pls add your numero:")) for j in range(cols)] for i in range(rows)]
rows2=int(input("how many rows do you want?:"))
cols2=int(input("how many columns do you want?:"))
MAT2 = [[int(input(f"for position {i},{j} pls add your numero:")) for j in range(cols)] for i in range(rows)]
res = [[MAT[i][j]+MAT2[i][j] for j in range(len(MAT[0]))] for i in range(len(MAT))]
for r in res:
    print(r)