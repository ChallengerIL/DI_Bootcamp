// Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

// 1
let number = prompt ("Please provide a number");
console.log(typeof(number))

// 2
const getNumber = function () {
    let number;
    
    do {
      number = prompt("Please provide a number");
    } while (number < 10);
  
    return number;
  };
  
  console.log(getNumber());
