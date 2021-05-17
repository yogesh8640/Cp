def isvovel(ch):
    return (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u')
string=input()
x=0
n=len(string)
vovelsubstring=""
while(x<n):
    if(isvovel(string[x])==False):
        x+=1
        continue
    temp=""
    while(x<n):
        if(isvovel(string[x])):
            temp+=string[x]
            x+=1
        else:
            break
    if(len(vovelsubstring)<len(temp)):
        vovelsubstring=temp
if(len(vovelsubstring)==0):
    print("-1")
else:
    print(vovelsubstring)
           
