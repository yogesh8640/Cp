def conso_vovels(word):
    for i in range(0,len(word)):
        if((i%2==0 and word[i] not in vovels) or (i%2==1 and word[i] in vovels)):
            pass
        else:
            return 0
    return 1

def vovels_conso(word):
    for i in range(0,len(word)):
        if((i%2==0 and word[i] in vovels) or (i%2==1 and word[i] not in vovels)):
            pass
        else:
            return 0
    return 1

    
vovels=['a','e','i','o','u']
w=input()
words=w.split(',')
for word in words:
    word=word.lower()
    res1=conso_vovels(word)
    res2=vovels_conso(word)
    if(res1==1 or res2==1):
        print("valid")
    else:
        print("invalid")

