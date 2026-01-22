n = int(input())
k = 1 
for i in range(1,n+1):
    ans=''
    for j in range(1,n+1):
        ans = ans+(str(k)+" ")
        k += 1
    print(ans)