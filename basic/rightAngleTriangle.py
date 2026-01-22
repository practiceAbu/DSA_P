n = 5

for col in range (1,n+1):
    val = ''
    for row in range(1,col+1):
        val = val +(str(row)+' ')
    print(val)