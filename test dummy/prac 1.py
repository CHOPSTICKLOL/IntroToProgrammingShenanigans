n_sales=int(input("how many loads have you sold:"))
bar=[]
cnt=0
ass=0
for x in range(n_sales):
    id=input(f"pls add the barcode num {x+1}")
    bar.append(id)
for i in bar:
    if len(i)==8:
        cnt=cnt+1
    elif len(i)==9:
        ass=ass+1
print(f"we sold {cnt} vinyls, we sold {ass} cds")