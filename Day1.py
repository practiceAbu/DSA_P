#You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

array = [2,4,6]
# Brute Force approch
def squareNumberASC(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        
    new_array.sort()
    
    return new_array
    
print(squareNumberASC(array))

