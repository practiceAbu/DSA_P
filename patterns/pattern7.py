n = 5
for col in range(n):
    for row in range(n,col,-1):
        print(n-row+1,end=" ")
    print()