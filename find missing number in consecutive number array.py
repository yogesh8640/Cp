t=int(input())
while(t!=0):
    n=int(input())
    list_element=list(map(int,input().split()))
    total=(n*(n+1))/2
    sum_total=sum(list_element)
    print(int(total-sum_total))
    t-=1
