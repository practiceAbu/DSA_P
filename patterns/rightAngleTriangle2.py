n = int(input())
for i in range(1,n+1):
    space = " "*(n-i)
    slash ="/"
    space2 =" "*(i-1)
    pipe = "|"
    if i == n:
       space2 ="_"*(i-1) 
    print(space+slash+space2+pipe)
