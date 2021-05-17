import math
list_num=input().split(',')
digit_sum_list=[]
for num in list_num:
    digit_sum=sum(list(map(int,num)))
    digit_sum_list.append(digit_sum)
max_sum=max(digit_sum_list)
lst_digit_count=[0]*(max_sum+1)
for num in digit_sum_list:
    lst_digit_count[num]+=1
total_pair=0
for count in lst_digit_count:
    if(count>1):
        total_pair+=int(math.factorial(count)/(math.factorial(count-2)*2))
if(total_pair==0):
    print("-1")
else:
    print(total_pair)
