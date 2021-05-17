import math
s=input()
temp=set()
res=[]

for i in range(0,len(s)):
    for j in range(i,len(s)):
        substr=int(s[i:j+1])
        temp.add(substr)

temp=sorted(list(temp))
for ele in temp:
    for val in range(0,int(math.sqrt(ele)+1)):
                     if(val * (val+1) ==ele):
                         res.append(ele)

print(res)
                     
