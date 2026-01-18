
x = 121 

def checkPalindrome(x) -> bool:
    if x  < 0 :
        return False
    rev = 0 
    xcopy = x
    while x != 0:
        rev = (rev * 10)+(x % 10)
        x //=10
    return rev == xcopy
    

print(checkPalindrome(x))