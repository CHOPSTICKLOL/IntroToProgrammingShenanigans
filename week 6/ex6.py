word,letter= input("input a word:"), input("input a letter")
counter= 0
for i in range(len(word)):
    if word[i] == letter:
        counter+=1
print(f"the letter appeared {counter} times")