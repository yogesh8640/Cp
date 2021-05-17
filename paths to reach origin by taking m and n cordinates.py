import math
t=int(input())
while(t!=0):
    x,y=list(map(int,input().split()))
    facttotal=math.factorial(x+y)
    factsum=math.factorial(x)*math.factorial(y)
    print(int(facttotal/factsum))
    t-=1
