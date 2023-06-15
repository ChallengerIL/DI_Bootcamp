// Exercise 1 : List Of People
// Instructions
// const people = ["Greg", "Mary", "Devon", "James"];


// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that gives the index of “Foo”. Why does it return -1 ?

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?


// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// Hint: take a look at the break statement in the lesson.

// Part I
// 1
const people = ["Greg", "Mary", "Devon", "James"];
const index = people.indexOf('Greg');
people.splice(index, 1);
console.log(`People: ${people}`);

// 2
const secondIndex = people.indexOf('James');
people.splice(secondIndex, 1, 'Jason');
console.log(`People: ${people}`);

// 3
people.push('My name');
console.log(`People: ${people}`);

// 4
const marysIndex = people.indexOf('Mary');
console.log(`Mary's Index is ${marysIndex}`);

// 5
const newPeople = people.slice(1, -1);
console.log(`New People: ${newPeople}`);

// 6
const fooIndex = people.indexOf('Foo');
console.log(`Foo's index: ${fooIndex}`);
// -1 means "no match found".

// 7
last = people.at(-1);
console.log(`The last element: ${last}`);


// Part II
// 1
people.forEach(name => console.log(name));

// 2
for (let name of people) {
    if (name == "Devon") {
        console.log(name);
        break;
    } else {
        console.log(name);
    }
}
