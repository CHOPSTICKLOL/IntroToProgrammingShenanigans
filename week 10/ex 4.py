x=["ann","mary","jane","sue"]
f=[a+" "+y for a in x for y in x if a!=y]
print(f)