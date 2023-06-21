// Exercise 1: Timer
// Instructions
// Using this HTML code:

// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         p {
//           background: yellow;
//           color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="container"></div>
//         <button id="clear">Clear Interval</button>
//     </body>
//     </html>


// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.


// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.


// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

// 1
function greetingAlert() {
    alert("Hello World");
}

setTimeout(greetingAlert, 2000);

// 2
let div = document.querySelector("#container");

function addText() {
    let p = document.createElement('p');
    p.appendChild(document.createTextNode('Hello World'));
    div.appendChild(p);
}

setTimeout(addText, 2000);

// 3
let timer = setInterval(addText, 2000);

let button = document.querySelector('#clear');
button.addEventListener('click', function() {clearInterval(timer)});

setInterval(function() {

    let paragraphs = div.querySelectorAll('p');

    if (paragraphs.length > 4) {
        clearInterval(timer);
    }

}, 1500);

