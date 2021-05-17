s=input()
s1=""
for i in range (len(s)-1,-1,-1):
    if s[i].isalnum():
        s1=s1+s[i]
s1=list(s1)
for i in range(len(s)):
    if s[i].isalnum()==False:
        s1.insert(i,s[i])
print("".join(s1))
