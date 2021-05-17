string_input=input()
lst=string_input.split(",")
string=lst[0]
ch=lst[1]
substring_list=string.split(ch)
total_substring=0
for substr in substring_list:
    length=len(substr)
    total_substring+=(length*(length+1))/2
print(int(total_substring))
