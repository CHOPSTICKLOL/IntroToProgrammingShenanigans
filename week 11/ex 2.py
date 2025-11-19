rows=int(input("how many rows do you want?:"))
cols=int(input("how many columns do you want?:"))
MAT = [[int(input(f"for position {i},{j} pls add your numero:")) for j in range(cols)] for i in range(rows)]
print(MAT)
