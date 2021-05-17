num=int(input())
list_num=list(map(int,input().split(" ")))
list_count=[]
set_unique=set(list_num)
for i in set_unique:
    count=list_num.count(i)
    list_count.append(count)
list_count.sort()
length=len(list_count)
for count in list_count:
    if(count<=num):
        num=num-count
        length=length-1
    else:
        break
print(length)
