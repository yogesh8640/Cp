t=int(input())
while(t!=0):
    string=input()
    stack=[]
    for digit in string:
        if(digit.isnumeric()):
            stack.append(digit)
        else:
            num1=int(stack.pop())
            num2=int(stack.pop())
            output=0
            if(digit=='*'):
                output=num2*num1
            elif(digit=='+'):
                output=num2+num1
            elif(digit=='-'):
                output=num2-num1
            else:
                output=int(num2/num1)
            stack.append(output)
            
    print(stack[0])
    t-=1
            
