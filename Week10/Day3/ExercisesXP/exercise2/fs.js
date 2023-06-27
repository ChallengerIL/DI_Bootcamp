// Exercise 2 : Writing Files With Node JS
// Instructions
// Create an fs.js file, and use the Node js File System to create a new text file and write to it.

// Use the Node js File System to append some other text to the text file. (Example:”Buy orange juice”)

// Use the Node js File System to delete the file.

let fs = require('fs');

// 1
fs.writeFile('data.txt', 'Bla Bla', function (err) { 
    if (err){ 
        console.log(err);
    }
});

// 2
fs.appendFile('data.txt', '\n' + "Buy orange juice", function (err) {
    if (err) {
        console.error(err)
        return
    }
});

// 3
fs.unlink('data.txt', function (err) {
    console.log('Deleted.');
});
