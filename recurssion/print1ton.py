def printNumber(current,n):
    if current > n:
        return
    print(current,end=" ")
    printNumber(current+1,n)

printNumber(1,10)
print()