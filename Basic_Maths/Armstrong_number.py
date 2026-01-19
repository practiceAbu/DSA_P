x = 153
copy = x
arm = 0
while x != 0:
    dig = x % 10
    arm = arm + dig ** 3 
    x //=10

if copy == arm:
    print(True)
else:
    print(False)