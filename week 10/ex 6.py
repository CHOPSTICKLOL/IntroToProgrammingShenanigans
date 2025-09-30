card=[int(input("insert 3 integers between 1 and 90"))for idx in range (3)]
import random
bingo=[random.randint(1,90)for i in range (70)]
hits=[e for e in card if e in bingo]
print(hits)
if len(hits)==3:
    print("threengo")
    print(hits)
else:
    print(f"better luck next time, you only got these:{hits}")