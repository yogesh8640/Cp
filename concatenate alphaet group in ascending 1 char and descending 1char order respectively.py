string_list=list(input())
char_list=[]
for i in range(len(string_list)):
    if(string_list[i]==''):
        continue
    char_grp=string_list[i]
    for j in range(i+1,len(string_list)):
        if(string_list[i].lower()==string_list[j].lower()):
            char_grp+=string_list[j]
            string_list[j]=''
    string_list[i]=''
    char_list.append(char_grp)
for i in range(len(char_list)):
    for j in range(i+1,len(char_list)):
        if(char_list[i].lower()>char_list[j].lower()):
            temp=char_list[j]
            char_list[j]=char_list[i]
            char_list[i]=temp
length=len(char_list)
for i in range(length//2):
    print(char_list[i]+char_list[length-i-1],end='')
if(length%2!=0):
    print(char_list[length//2])
                       
                       
