def calculator(string):
    length=len(string)
    str1=list(string)
    for i in range(length):
        if(str1[i]=='#'):
            for j in range(i-1,-1,-1):
                if(str1[j].isalpha()):
                    if(str1[j]=='Z'):
                        str1[j]='A'
                        break
                    else:
                        str1[j]=chr(ord(str1[j])+1)
                        break
    return (''.join(str1))
    
t=int(input())
while(t!=0):
    str1=input()
    str2=input()
    s=calculator(str1)
    s2=calculator(str2)
    string1=''.join(s.split("#"))
    string2=''.join(s2.split("#"))
    if(string1==string2):
        print("yes")
    else:
        print("No")
    t-=1
    
    
