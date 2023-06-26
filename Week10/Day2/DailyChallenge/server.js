// Instructions
// Use Express to create a few routes:
// The route /aboutMe/:hobby sends the name of one hobby (ie. the value of the route parameter). If the parameter is not a string (ie. numbers or else), set the status to 404.
// The route /pic : displays an HTML file with a picture of your choice.
// The route /form: displays an HTML file.
// Requirements:
// The HTML file must be in the public folder.
// The HTML file must contain a form to contact you.
// The form must contain the inputs email and message. (add some HTML form validations)
// Output:
// You should get the data and display it on the browser at the route /formData.
// For example, “john@gmail.com sent you a message “Love your new website”.

const express = require('express');
const path = require('path');
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/aboutMe/:hobby', (req, res) => {
    if (isNaN(req.params.hobby)){
        res.send(req.params.hobby);
    } else {
        res.status(404).send("Something went wrong...");
    }
});

app.get('/pic', function (req, res) {
    res.sendFile(path.join(__dirname+'/public/pic.html'));
});

app.get('/form', function (req, res) {
    res.sendFile(path.join(__dirname+'/public/form.html'));
});

app.post('/formData', (req, res) => {
    res.send(`${req.body.email} sent you a message “${req.body.message}"`);
});

app.listen(3000);
