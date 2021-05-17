num=int(input())
num+=1
while(True):
    if(str(num)==str(num)[::-1]):
        print(num)
        break
    else:
        num+=1
