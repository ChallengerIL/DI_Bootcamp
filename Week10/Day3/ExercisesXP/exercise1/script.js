// Exercise 1 : Reading From A File In Node.JS
// Instructions
// Create a text file and write something inside (example: ‘Some Text To See’)
// Create an fs.js file, and inside use the Node JS File System to read the text file and console.log the output in the terminal

let fs = require('fs');

fs.writeFile('test.txt', 'Some Text To See', function (err) { 
    if (err){ 
        console.log(err);
    }
});
