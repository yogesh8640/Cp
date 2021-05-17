from collections import Counter
s1=input()
s2=input()
d1=Counter(s1)
d2=Counter(s2)
print(len((d1|d2)-(d1&d2)))
