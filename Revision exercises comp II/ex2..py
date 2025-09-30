def lucas_buttler(d):
    for number in range(len(d)-1):
        if d[number]>d[number+1]:
            return False
    return True
dipto=[1,7,4,5,6]
print(lucas_buttler(dipto))
#we decide to use for loops
# it iterates through all the numbers and d helps us get an actual position
