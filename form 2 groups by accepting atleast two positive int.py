a=list(map(int,input().split(',')))
n1=len(a)
n2=n1//2
su=sum(a)/2
dp=[[-1 for i in range(n2+1)] for j in range(n1)]
def answer(i,n,s):
    if i<(n-1):
        return float('inf')
    if n==0:
        return abs(s)
    else:
        return min(answer(i-1,n-1,s-a[i-1]),answer(i-1,n,s))
k=answer(n1-1,n2,su)
print(int(su-k),int(su+k))
