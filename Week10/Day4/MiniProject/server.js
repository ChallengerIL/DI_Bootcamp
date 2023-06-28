// Instructions
// Part I: HTML Page
// Create an HTML page containing two forms:

// Register form : first name, last name, email, username and password
// Login form : username and password
// forms

// Part II : Requirements
// Make sure to disable any submit button if an input is empty.

// Use javascript to retrieve the inputs and fetch your server for the register and login routes.

// Use Node.js to create an express server and knex to communicate and store the new data in the database.

// Part III: The Database And Tables
// You will store the data in two different tables with PostgreSQL.

// tables

// Register Table
// The Register table should have the following columns: user id, first name, last name, a unique email, username, created date (ie. date when the user registered), last login date (ie. date when the user last logged in).

// Use p4ssw0rd to encrypt the password.

// When a user registers correctly and the data gets stored in the database display a message which states that the registration was successfull. For example:

// register

// user table

// 4. When the registration was not successfull display a message with the issue for example if an email already exists in the database:

// already exists

// Login Table
// The Login table should have the following columns: login id, username and password.

// When the user logs in successfully display a success message:

// login success

// login table

// 3. When the login wasnt successful, display a message stating the issue : for example if they are trying to login without beeing registered first.

// not exist

const express = require('express');
const path = require('path');
let cors = require("cors");
const bp = require('body-parser');
const app = express();

const password_hash = require('p4ssw0rd');

const db = require('knex')({
    client: 'pg',
    connection: {
        host: '127.0.0.1',
        user: 'postgres',
        password: 'postgres',
        database: 'users',
        port: 5432
    }
});

app.set("db", db);
app.use(cors());
app.use(express.static(path.join(__dirname, "public")));
app.use(bp.urlencoded({extended:false}));
app.use(bp.json());

app.get('/', (req, res) => {
    res.render('index');
})

function createUser(user){
    user.password = password_hash.hash(user.password);

    return db('register')
    .returning(['user_id', 'first_name', 'last_name', 'email'])
    .insert(
       user
    )
    
  }

app.post('/register',(req,res)=>{
    createUser(req.body)
    .then(data => {
        res.send(data)
    })
    .catch(err => {
        res.send({message:err.detail})
    })
})

app.post('/login',(req,res)=>{
    const {username,password} = req.body;
    
    db('register')
    .select('user_id','username','password')
    .where({username:username})
    .then(data => {
        if(data.length>0){
            if(password_hash.check(password, data[0].password)){
                
                db('login')
                .insert({ username: username, password: password})
                .then(res.send(
                        {
                            message:`OK Hello your username is ${username}`
                        }
                        )
                )
            }
        else{
            res.send({message:'Wrong password'})
        }
        }
        else {
        res.send({message:'User Not Found'})
        }
    })
    .catch(err => {
        res.send({message:err.detail})
  })
})

app.listen(3000);
