from itertools import permutations
s=input("enter the string")
perm=list(permutations(s))
for tup in perm:
    print(''.join(tup))
