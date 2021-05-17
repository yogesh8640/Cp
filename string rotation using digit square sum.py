def Rotate(string,num):
    sum=0
    while(num>0):
        sum+=(num%10)**2
        num=num//10

    if sum%2==0:
        print(string[-1]+string[:-1])
    else:
        print(string[2:]+string[:2])

s=input().split(',')
for x in s:
    string,num=x.split(':')
    num=int(num)
    Rotate(string,num)
