// Exercise 3 : Analyzing
// Instructions
// Analyze these pieces of code before executing them. What will be the outputs ?
// ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// ------2------
// const country = "USA";
// console.log([...country]);

// ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);

// 1
// Everything will be unpacked into a regular array, no nesting.

// 2
// The string will be converted to an array of characters from the original string.

// Bonus
// We will get an array of two undefined values, because the original array doesn't contain anything but two commas.
