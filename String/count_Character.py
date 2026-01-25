s = input()
val = int(input())
count = 0 
for i in s:
    ans = ord(i)    
    if val ==ans:
        count = count+1

print(count)