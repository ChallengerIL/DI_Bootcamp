const user = {firstname: 'John',lastname: 'Doe'};

const express = require('express');
let cors = require("cors");
const app = express();

app.use(cors());

app.get('/users', (req, res) => {
    res.json(user);
})

app.listen(3000);
