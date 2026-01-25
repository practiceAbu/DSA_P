n = int(input())
v = []
for i in range(1,n+1):
    v.append(int(input()))
    
ans = ""
for j in v:
    ans = ans + chr(j)

print(ans)