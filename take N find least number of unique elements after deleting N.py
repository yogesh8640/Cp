rem=int(input())
list_num=list(map(int,input().split(",")))
distinct = set(list_num)
print(len(distinct)-rem) 
