// Exercise 5 : Event Listeners
// Instructions
// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.

const height = document.documentElement.clientHeight;
const width = document.documentElement.clientWidth;
let div = document.querySelector('div');

div.addEventListener("click", () => {
    let randY = Math.floor((Math.random() * height) + 1);
    let randX = Math.floor((Math.random() * width) + 1);
    div.style.transform = `translate(${randX}px, ${randY}px)`;
});

div.addEventListener("mouseover", () => {
    div.style.background = 'blue';
});

div.addEventListener("mouseout", () => {
    div.style.background = 'red';
});

div.addEventListener("dblclick", () => {
    div.style.border = '1rem yellow solid';
});
