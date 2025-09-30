from random import randint

card = [int(input(f"Enter number {i + 1} [1,90]: ")) for i in range(3)]
bingo = [randint(1, 90) for i in range(70)]
hits = [h for h in card if h in bingo]
if len(hits) == 3:
    print(f"THREENGO!! Numbers chosen: {card}")
else:
    print(f"Better luck with next card! Numbers chosen: {card}, hits: {hits}")
