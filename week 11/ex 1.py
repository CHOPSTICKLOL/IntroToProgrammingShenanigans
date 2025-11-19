M=[[5,4],[3,5],[1,2],[0,0]]
print(M[1][0],M[2][1])
sum= M[0][0]+M[0][1]+M[3][0]+M[3][1]
print(sum)
print(f"the number of rows is {len(M)} and the number of columns is {len(M[0])}")
count=0
for row in M:
    for col in row:
        if col>3:
            count+=1
print(f"there are {count} numbers which are bigger than 3")
