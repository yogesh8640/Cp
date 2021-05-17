from itertools import permutations
s=input("enter the string")
for length in range(1,len(s)+1):
    perm=list(permutations(s,length))
    for tup in perm:
        print(''.join(tup))
print(len(tup))
