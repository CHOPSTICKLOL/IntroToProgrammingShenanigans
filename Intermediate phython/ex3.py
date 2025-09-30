def letter_counter(gg):
    dic={}
    for letter in gg:
        dic[letter]=(gg.count(letter))
    return dic
word="sameeeeeeeeeeeeeeeer"
print(letter_counter(word))


