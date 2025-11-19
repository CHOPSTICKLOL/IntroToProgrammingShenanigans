ppl=int(input("enter how many ppl will work"))
salaries = [int(input("enter salary")) for i in range(ppl)]
print(salaries)
bonus = [x+500 for x in salaries]
print(bonus)