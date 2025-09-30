word=input("giv me weed:")
counter=0
for letter in word:
    if letter not in "aeiou":
        counter+=1
print(counter)