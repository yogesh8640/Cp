def check_balance(exp):
    mylist=[]
    for char in exp:
        if(char in ['(','[','{']):
            mylist.append(char)
        else:
            if(len(mylist)==0):
                return False
            cur_char=mylist.pop()
            if(cur_char=='('):
                if(char!=')'):
                    return False
            if(cur_char=='['):
                if(char!=']'):
                    return False
            if(cur_char=='{'):
                if(char!='}'):
                    return False
    if(len(mylist)>0):
       return False
    else:
        return True

exp=input()
if(check_balance(exp)):
    print("exp is balanced")
else:
    print("exp is unbalanced")
            
    
