
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    last = fibonacci(n-1)
    slast = fibonacci(n-2)

    return last + slast

print(fibonacci(5))

def fibonacci2(n):
 ans =[0, 1]
 if n == 0 or n == 1:
    return n
 for i in range (2,n+1):
    ans.append(ans[i-1]+ans[i-2])
 return ans[n]
print(fibonacci2(5))
