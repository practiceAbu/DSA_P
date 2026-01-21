a = input()
leng = len(a)
n = int(a)
val = 0
while n != 0:
    dig = n % 10
    val = dig ** leng + val
    n //=10
print(val)