// Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:

// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>


// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the <article> tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

const h1 = document.getElementsByTagName("h1")[0].innerHTML;
console.log(h1)

const lastP = document.querySelector("article").lastElementChild;
lastP.remove();

let h2 = document.querySelector("h2");
h2.addEventListener("click", changeColor);
function changeColor() {
    h2.style.background = "red";
}

let h3 = document.querySelector("h3");
h3.addEventListener("click", hide);
function hide() {
    h3.style.display = "none";
}

let boldButton = document.querySelector("button[name='bold-button']");
boldButton.addEventListener("click", goBold);
function goBold() {
    let pArray = document.querySelectorAll('p');
    for (let p of pArray) {
        p.style.fontWeight = 'bold';
    }
}

