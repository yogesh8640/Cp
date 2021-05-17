string=input()
even,odd=[],[]
c=len(string)
for ch in string:
    if ch.isdigit():
        if int(ch)%2==0:
            even.append(int(ch))
        else:
            odd.append(int(ch))
    if isalnum():
        c-=1
begin,end=[],[]
if c%2==0:
    begin=even
    end=odd
else:
    begin=odd
    end=even

if(len(begin)>len(end)):
    for i in range(len(end)):
        print("{}{}".format(begin[i],end[i],end='')
    for num in begin[len(end):]:
        print(num,end='')
else:
    for i in range(len(begin)):
        print("{}{}".format(begin[i],end[i],end='')
    for num in end[len(begin):] :
        print(num,end='')
    
        
