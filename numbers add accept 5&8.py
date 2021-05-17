numbers=list(map(int,input().split(',')))
id5=numbers.index(5)
id8=numbers.index(8)
num1=sum(numbers[:id5]+numbers[id8+1:])
num2=0
for digit in numbers[id5:id8+1]:
    num2=num2*10+digit
print(num1+num2)
