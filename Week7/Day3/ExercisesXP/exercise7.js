// Exercise 7 : Secret Group
// Instructions
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// 1
function getFirstLetters(str) {
    const firstLetters = str
      .split(',')
      .map(word => word.charAt(0))
      .join('');
  
    return firstLetters;
  }

// 2
console.log(getFirstLetters(names.toString()));

