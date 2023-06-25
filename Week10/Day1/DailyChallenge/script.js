// import number from './main.js';

const a = require('./main.js').number;
const b = 5;
const result = a + b
const currentDate = require('./main.js').currentDate;

console.log(result);

let http = require("http");

const server = http.createServer(function (req, res) {
    console.log('I am listening');
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`<html><body><p>My Module is:<br>${result}</p><h1>Hi there at the frontend</h1></body></html>`);
}).listen(3000);

const anotherServer = http.createServer(function (req, res) {
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`<html><body><p>The date and time are currently: ${currentDate()}</p></body></html>`);
}).listen(8080);
