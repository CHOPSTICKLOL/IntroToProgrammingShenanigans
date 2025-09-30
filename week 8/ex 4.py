intnum=int(input("how many integers would you like to insert?"))
i=1
while i <= intnum:
    x=int(input(f"insert number{i}"))
    if x%2==0:
        print("even")
    else:
        print("odd")
    i+=1