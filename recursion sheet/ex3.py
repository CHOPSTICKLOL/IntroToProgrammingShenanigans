def chigga(a, n):
    if n==1:
        return a
    if a==1:
        return a
    return a*chigga(a, n-1)
nigga=2
higga=3
print(chigga(nigga, higga))



