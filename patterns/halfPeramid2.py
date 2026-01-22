n = int(input())

k = 1 

for col in range(1,n+1):
    val = ''
    for row in range(1,col+1):
        val = val + (str(k)+" ")
        k+=1
    print(val)