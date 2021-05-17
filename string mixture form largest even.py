strings=input()
numbers=[]
for each in strings:
    if each.isdigit() and int(each) not in numbers:
        numbers.append(int(each))
numbers.sort(reverse=True)
id= -1
n=len(numbers)
for i in range(n-1,0,-1):
    if numbers[i]%2==0:
        id=i
        break
if id==-1:
    print(-1)
else:
    num=0
    for i in range(n):
        if i==id:
            continue
        else:
            num=num*10+numbers[i]
    num=num*10+numbers[id]
    print(num)
            
    
