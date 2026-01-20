def sum(current,n):
    if current > n :
        return 0
    return current + sum(current+1,n)

val = sum(1,10)
print(val)
ans = 0
for i in range (1,11):
    ans += i

print(ans)
