number=input()
length=len(number)
otp=''
for i in range(length):
    if(int(number[i])%2!=0):
        otp+=str(int(number[i])**2)
if(len(otp)<4):
    print(-1)
else:
    print(otp[0:4])
                 
