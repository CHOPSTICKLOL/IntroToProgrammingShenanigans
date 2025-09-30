import math

my_string="My circle has a radius of 3, and my square has a length of 4.5."
sqr=my_string[-4:-1]
csqr=float(sqr)
circ=my_string[26]
ccirc=int(circ)
sa=csqr**2
sp=csqr*4
ca=math.pi*ccirc**2
cp=2*math.pi*ccirc
print(sa)
print(sp)
print(ca)
print(cp)

