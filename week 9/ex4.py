lst= ["Anthony", "Gertrude", "Gertrudo", "Anthonella"]
for i in lst:
    for char in i:
        if char.lower() in "aeiou":
         print("found a fucking vowel")