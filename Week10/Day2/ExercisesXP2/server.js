const user = {firstname: 'John',lastname: 'Doe'}

const express = require('express')
const app = express()

app.get('/users', (req, res) => res.send(JSON.stringify(user)))

app.listen(3000)