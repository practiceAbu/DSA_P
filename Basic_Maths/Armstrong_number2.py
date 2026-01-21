n = input()
ans = 0
leng= len(n)
a = int(n)
x = a
while a != 0:
    dig = a % 10
    ans = dig ** leng + ans
    a //=10

if ans == x:
    print(f"Armstrong Number {ans}")
else:
    print("Not Armstrong Number")