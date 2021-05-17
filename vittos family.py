n = int(input())

while (n):

    t = input().split(" ")
    print(t)
    r = t[0]
    t.remove(r)
    r = int(r)

    for i in range(0, r):
        t[i] = int(t[i])

    t.sort()
    mid = t[r // 2]
    result = 0
    for i in t:
        result += abs(i - mid)

    print(result)
    n -= 1
