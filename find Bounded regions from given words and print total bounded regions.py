import re
t=int(input())
while(t!=0):
    n=int(input())
    words=input()

    ones=re.findall("[abdegopq490oADRPQ^]",words)
    twos=re.findall("[88]",words)
    print(len(ones)+len(twos)*2)

    t-=1
