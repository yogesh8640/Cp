def factor(n):
    s=0
    if n==1:
        return 1
    for i in range(1,n):
        if n%i==0:
            s+=i
            return s
   
list1=list(map(int,input().split(',')))
flag=0
for i in list1:
    if factor(i) in list1:
        flag=1
        print(i)
#if sum is not present
if flag==0:
    print("-1")
