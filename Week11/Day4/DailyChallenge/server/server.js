const express = require('express');
const app = express();
const cors = require("cors");
const bp = require('body-parser');

app.use(cors());
app.use(bp.urlencoded({extended:false}));
app.use(bp.json());

app.get('/api/hello', (req, res) => res.send('Hello from Express'));

app.get('/test', (req, res) => {
    return res.send('Hello world!')
  })

app.post('/api/world', (req, res) => {
    console.log(req.body);
    
    return res.send(`I received your POST request. This is what you sent me: ${req.body.message}`)
});

app.listen(4000);