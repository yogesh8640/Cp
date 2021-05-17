t=int(input())
for _ in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    sr=sorted(ls)
    for num in ls:
        print(sr.index(num),end='')
    print()
            
