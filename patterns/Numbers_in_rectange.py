col = int(input())
row = int(input())
k = 1 
for i in range(1,col+1):
    val =''
    for j in range(1,row+1):
        val = val + (str(k)+" ")
        k = k + 1
    print(val)