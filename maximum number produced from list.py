from itertools import permutations
list_ele=input().split()
permutation_tuples=permutations(list_ele)
list_ele=[]
for tpl in permutation_tuples:
    value=int(''.join(tpl))
    list_ele.append(value)
print(max(list_ele))
