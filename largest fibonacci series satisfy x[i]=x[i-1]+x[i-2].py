list_number=list(map(int,input().split(",")))
length=len(list_number)
list_total=[]
for i in range(0,length):
    for x in range(i+1,length):
        first=list_number[i]
        second=list_number[x]
        fab_list=[]
        fab_list.append(first)
        fab_list.append(second)
        for y in range(x+1,length):
            if(first+second==list_number[y]):
                fab_list.append(list_number[y])
                first=second
                second=list_number[y]
        if(len(list_total)<len(fab_list)):
            list_total=fab_list
if(len(list_total)>2):
    for ele in list_total:
        print(ele,end=' ')
else:
    print("-1")
        
