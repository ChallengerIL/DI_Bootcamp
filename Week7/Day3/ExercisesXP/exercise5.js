// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

// 1
family = {
    husband: 'John',
    wife: 'Jane'
}

// 2
for (const status in family) {

    console.log(status);
    // console.log(`${status}: ${user[key]}`);
}

// 3
for (const status in family) {

    console.log(family[status]);
}
