// You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

// Brute Force Approch
function squareNumberASC(arr){
let newArray = new Array(arr.length).fill(0);
 for(let i = 0; i < arr.length;i++){
    newArray[i] = Math.pow(arr[i],2)
 }
 newArray.sort(function(a,b){
    return a-b;
 })
 return newArray;
}

a = [2,4,5]
console.log(squareNumberASC(a))