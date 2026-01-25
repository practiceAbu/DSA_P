n = int(input())

y = n // 365
remaining_days = n % 365
w = remaining_days // 7
D = remaining_days % 7

print(y)
print(w)
print(D)