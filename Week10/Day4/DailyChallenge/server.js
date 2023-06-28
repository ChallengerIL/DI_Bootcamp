// Instructions: Login And Register With Node Js
// Create 2 HTML files: one for the Login form and the other for the Register form (when the inputs are empty the submit button should be disabled).

// Create a server with Node.js and express.

// Write the users data to a JSON file.

// In a script.js file, set up all the server functionalities and the fetches for the corresponding forms.

// The Register form should have five inputs: Name, Last Name, Email, Username and Password. And it should register a user with a message as follows:
// register

// When the user registers, if the username or the password already exist, do not write to the file. Instead, send a message back as follows:
// error1

// The Login form should have two inputs: Username and Password. And it should display a login message as follows:
// login

// When the user logs in and if they are not registered, send and error message as follows:
// error2

const express = require('express');
const app = express();
const fs = require("fs")
let cors = require("cors");
const bp = require('body-parser');
const engines = require('consolidate');
const password_hash = require('p4ssw0rd');

app.use(cors());
app.use(express.static(__dirname + '/public'));
app.use(bp.urlencoded({extended:false}));
app.use(bp.json());
app.set('views', __dirname + "/public");
app.engine('html', engines.mustache);
app.set('view engine', 'html');

function checkfile(file) {
    if (!file.includes(".")) {
        return fs.existsSync(`public/${file}.html`);
    }
    return fs.existsSync(`public/${file}`);
}

app.get('/:filename', (req, res) => {
    let filestring = req.params.filename.toString()
    if (checkfile(filestring)) {
        res.render(filestring)
    }
});

app.post('/register', (req, res) => {
  let users = [];
  let newUser = req.body;
  try{
    const f = fs.readFileSync('./users.json');
    users = JSON.parse(f)

    if (users.length > 0) {
        users.forEach((user) => {
            if (newUser.username == user.username) {
                throw new Error("Username already exists");
            } else if (newUser.email == user.email) {
                throw new Error("Email already exists");
            }
        })
    }
  }
  catch(e){
    return res.send({message: e.message});
  }
  finally{
    newUser.password = password_hash.hash(newUser.password);
    users.push(newUser)
  }

  fs.writeFile('./users.json', JSON.stringify(users), err=>{
    if(err){
      console.log('error writing to file');
    }
  })

  res.send({message:'Hello! Your account is now created!'})
});

app.post('/login', (req, res) => {
    const {username,password} = req.body;
    
    try{
      const f = fs.readFileSync('./users.json');
      let users = JSON.parse(f);
      let matchFound = false;
  
      if (users.length > 0) {
        users.forEach((user) => {
            if (username == user.username) {
                matchFound = true;
                if (password_hash.check(password, user.password)) {
                    res.send({message:`Hi ${username}, Welcome back again!`});
                } else {
                    throw new Error("Wrong password.");
                }
            }
        })
        
        if (!matchFound) {
            throw new Error("Username is not registered.");
        }
        }
    }
    catch(e){
      return res.send({message: e.message});
    }
  });

app.listen(3000);
