def isPalendrome(num):
    return str(num)[::-1]==str(num)
def rev(num):
    return int(str(num)[::-1])
num=int(input())
while(1):
    num=num+rev(num)
    if(isPalendrome(num)):
        print(num)
        break;
    
