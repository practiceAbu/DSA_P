count = 0
n = int(input("Please enter the input : "))
for i in range (1,n+1):
    if n % i == 0:
        count += 1
    

if count == 2:
    print('prime')
else:
    print('Not prime')

