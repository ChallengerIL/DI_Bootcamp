// Instructions
// Download this Github repository.

// Create an fs.js file and use the Node js File System to read the RightLeft file. In the file, you will see a list of symbols : > and <. Each one of this symbol has a meaning:
// > means that you move 1 step to the right
// < means that you move 1 step to the left

// Example:

// When you start reading the file, you start at the position 0
// If the file begins like this ">>>" after 3 steps you would be in position 3
// If the file begins like this ">>><<" after 5 steps you would be in position 1


// Use the corresponding operations to calculate the final position at the end of the file - The answer should be: 74 steps to the right.


// Use the corresponding operations to calculate the number of steps needed to hit position the -1 for the first time - The answer should be: 1795 steps.

let fs = require('fs');
fs.readFile('RightLeft.txt', 'utf-8', function (err, data) {
    if (err) {
        console.error(err)
        return
    }
    
    let counter = 0;

    // 1
    for (let symbol of data) {
        if (symbol == ">") {
            counter++;
        } else if (symbol == "<") {
            counter -= 1;
        }
    }

    // 2
    // The number of steps is always gonna be positive. How can we possibly hit -1?

    console.log(`Total steps: ${counter}`);

});

