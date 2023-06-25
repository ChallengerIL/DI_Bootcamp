// Instructions
// Part I:
// Create a file named main.js that contains a variable const largeNumber = 356; and export the module.

// Use the exported module in a script.js file.

// In the script.js file declare a variable const b = 5; and use it to output the sum of the imported module + b
// Expected Output
// 1



// Part II:
// Before starting the exercises, check out the lesson named Node.js Application in the Course Notes.

// In the script.js file create a server using the http module (require('http')).

// Create a server instance and bind it at port 3000. Therefore your server should run on http://localhost:3000/. When the server run, you should console.log("I'm listening") in the terminal.

// Set the response header to res.setHeader('Content-Type', 'text/html')(look at this tutorial- Part named “Serving HTML)

// Respond (res.end) with a HTML paragraph saying "My Module is <result from Part I>", and an HTML <h1> saying “Hi there at the frontend”

// Expected Output
// 2



// Part III:
// In the main.js, create a function that returns the current date and time. Export the module.

// Use the exported module in a script.js file.

// Create a server with http and set the response header to 'text/html'. Respond with an HTML paragraph that outputs the current date and time from the exported module.

// Your server should run on http://localhost:8080/
// Expected Output in HTML
// 3

const largeNumber = 356;

function getCurrentDate() {
    return Date();
};


// export const number = largeNumber;

module.exports = {
    number : largeNumber,
    currentDate: getCurrentDate
}
