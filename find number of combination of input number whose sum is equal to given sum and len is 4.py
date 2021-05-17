import itertools
input_set=list(map(int,input().split(",")))
s=int(input())
lst_combination=list(itertools.combinations(input_set,4))
count=0
for obj in lst_combination:
    obj_sum=sum(obj)
    if(obj_sum==s):
        count+=1
if(count==0):
    print("-1")
else:
    print(count)
