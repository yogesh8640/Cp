string=input()
input_list=string.split(",")
result=""
for i in input_list:
    string,number=i.split(":")

    length=len(string)
    sum=0
    for digit in number:
        sum+=(int(digit)**2)

    if(sum%2==0):
        sub=string[length-2:length]
        result=sub+string[0:length-2]
    else:
        sub=string[0]
        result=string[1:length]+sub
    print(result,end=' ')
