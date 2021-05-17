s=input()
ct=0
vt=0
v=['a','e','i','o','u']
if(s[0] in v):
    vt=1
else:
    ct=1

arr=[]
i=0
length=len(s)
my_new=""
while True:
    if(i==length):
        my_new +=max(arr)
        break
    if(vt):
        if(s[i] in v):
            arr.append(s[i])
            i+=1
        else:
            my_new+=max(arr)
            ct=1
            vt=0
            arr=[]
    else:
        if(s[i] not in v):
            arr.append(s[i])
            i+=1
        else:
            my_new+=max(arr)
            ct=0
            vt=1
            arr=[]
if(len(my_new)<3):
    print('X')
else:
    print(my_new)
