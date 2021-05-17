from itertools import combinations
t = int(input())
distinct_subarray = set()
while(t != 0):
    n = int(input())
    lst_input = list(map(int,input().split(',')))
    for i in range(n):
        sum = lst_input[i]
        string =''
        if(sum % 2 != 0):
            distinct_subarray.add(str(sum))
        string+=str(sum)
        for j in range(i+1,n):
            sum+=lst_input[j]
            string+=str(lst_input[j])
            if(sum % 2 != 0):
                distinct_subarray.add(string)
    t-=1
print(len(distinct_subarray))
#input:
#1
#3
#1,2,3

#output
#4
