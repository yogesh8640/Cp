fibbo = []
f1 = 1
f2 = 1
fibbo.append(f1)
fibbo.append(f2)


for i in range(0, 100000):
    temp = f1 + f2
    fibbo.append(temp)
    f1 = f2
    f2 = temp

z = input().split(" ")
a = int(z[0])
b = int(z[1])

count = 0
if (a <= 1):
    count = 2

for temp in fibbo:
    if(temp >= a and temp <= b):
        count+=1

print(count)
