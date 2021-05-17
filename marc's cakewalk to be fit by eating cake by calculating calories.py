n=int(input().strip())
calories=list(map(int,input().strip().split(' ')))
calories.sort(reverse=True)
ans=0
for x in range(0,n):
    ans=ans+(2**x)*calories[x]
print(ans)
