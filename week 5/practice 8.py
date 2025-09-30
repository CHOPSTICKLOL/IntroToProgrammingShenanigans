name = input("Insert your name: ")
if name[-1]=="a":
 name = name[:-1]+"inha"
 print(f"Nice to meet you {name}")
elif name[-1]=="o":
 name = name[:-1] + "inho"
 print(f"Nice to meet you {name}")
else:
 print(f"Nice to meet you {name}")

