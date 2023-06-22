// Exercise 2 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
// Then, use function expression and invoke it.
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.

// 1
function kilosToGrams(weight) {
    return weight * 1000;
}         
console.log(kilosToGrams(2));

// 2
let kilosToGrams = function (weight) {
    return weight * 1000;
}         
console.log(kilosToGrams(2));

// 3
// Function expressions don't have a name and they are assigned to a variable

// 4
const kilosToGrams = (weight) => {
    return weight * 1000;
  }
  
console.log(kilosToGrams(2));
