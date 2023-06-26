const express = require('express');
let cors = require("cors");
const app = express();

app.use(cors());

app.get('/:id', (req, res) => {
    console.log(req.params)
    res.send(req.params)
})

app.listen(3000);
