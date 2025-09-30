caps=0
while caps<2:
    password=input("write pass:")
    caps=0
    for letter in password:
        if letter.isupper():
            caps+=1

