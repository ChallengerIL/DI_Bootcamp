// Exercise 3: Express & Static Files
// Instructions
// Create a public folder, that contains an HTML file. This HTML file can contain some CSS and some JavaScript (for example a head tag with some classes for styling, and in the body a button with an onClick attribute calling a Javascript function with an alert).
// In a server.js file create your server using express.
// Your server on http://localhost:3000/ should serve the HTML file. Check out the lesson named Express Routes & Queries in the Course Notes, more specifically the part “How To Serve Static Files In Express”

const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/', (req, res) => {
})

app.listen(3000);

// const express = require('express');
// let cors = require("cors");
// const app = express();

// app.use(cors());

// app.get('/', (req, res) => {
//     // console.log(req.params)
//     // res.send(req.params)
// })

// app.listen(3000);
