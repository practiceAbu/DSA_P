s = input()
ans = 0
for i in s:
    if(ord(i) < 96) :
        ans = ord(i)
        break


print(ans)