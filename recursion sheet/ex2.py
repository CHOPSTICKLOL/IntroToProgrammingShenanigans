def adder(n):
    if n==1:
        return 1
    else:
        return n+adder(n-1)
leander=10
print(adder(leander))


