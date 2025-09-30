nome=input("pls name your pet:")
sel=int(input(f"what type of animal is {nome}?, 1 for dawg 2 for el gato and 3 for else"))
if sel==1:
    print(f"your {nome} dawg will need {50+(50*0.23)}euro for its treatment")
elif sel==2:
    print(f"your {nome} gato will need {40+(40*0.23)} euro for treatment" )
elif sel==3:
    print(f"your {nome} animal will need {60+(60*0.23)} euro for its treatment")
else:
    print("invalid input")
