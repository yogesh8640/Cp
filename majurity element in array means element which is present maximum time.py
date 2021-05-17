t=int(input())
while(t!=0):
    n=int(input())
    count_list=[0]*(1000001)
    lst=list(map(int,input().split()))
    for i in lst:
        count_list[i]+=1
    max_value=max(count_list)
    if(max_value>n/2):
        idx=count_list.index(max_value)
        print(idx)
    else:
        print(-1)
    t-=1
