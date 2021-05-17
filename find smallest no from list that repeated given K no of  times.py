n=int(input())
lst=list(map(int,input().split()))
k=int(input())
count_lst=[0]*100001
for i in lst:
    count_lst[i]+=1
for i in range(100002):
    if(count_lst[i]==k):
        print(i)
        break
