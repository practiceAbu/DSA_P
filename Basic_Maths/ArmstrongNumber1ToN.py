n = int(input())

for i in range(1,n+1):
    ans = 0
    a = str(i)
    leng = len(a)
    num = int(leng)
    x = i
    while i != 0:
        dig = i % 10
        ans = ans + dig ** num
        i //=10
    if ans == x:
        print(ans)