string=input()
length=len(string)
half=length//2
for i in range(half,0,-1):
    prefix=string[0:i]
    suffix=string[length-i:length]
    if(prefix==suffix):
        flag=1
        break
if flag==1:
    print(prefix)
else:
    print(-1)
