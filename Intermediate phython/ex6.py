def converter(gg):
    try:
        gg= int(gg)
    except:
        return "i hate you"
    else:
        return gg
numero="453423"
print(converter(numero))