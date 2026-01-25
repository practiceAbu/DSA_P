s = input()

for i in s:
    val = ord(i)
    if (65 <= val <= 90) or (97 <= val <= 122) or (48 <= val <= 57) or i == '_':
       ans = True
    else:
       ans = False
       break

if ans:
   print(True)
else:
   print(False)