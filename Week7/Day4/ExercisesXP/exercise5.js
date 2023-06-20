// Exercise 5 : Users
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
// Change each first name of the two <ul>'s to your name. (Hint : use a loop)

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

// 2.1
console.log(document.getElementsByTagName("div")[0]);

// 2.2
document.querySelectorAll('ul > li:last-child')[0].innerHTML = "Richard";

// 2.3
let secondList = document.querySelectorAll('ul')[1];
secondList.removeChild(secondList.children[1]);

// for (const child of secondList.children) {
//     if (child.innerHTML === 'Sarah') {
//         secondList.removeChild(child);
//     }
//   }

// 2.4
let listArray = document.querySelectorAll('ul');
let myName = "My name";

for (const list of listArray) {
    for (let listItem of list.children) {
        if (listItem.innerHTML != myName) {
            console.log(listItem)
            listItem.innerHTML = myName;
        }
    }
}


// 3.1
for (const list of listArray) {
    list.classList.add("student_list");
}

// 3.2
listArray[0].classList.add("university", "attendence");


// 4.1
document.getElementById("container").style.background = "lightblue";

// 4.2
listArray[0].children[1].style.display = "none";

// 4.3
listArray[0].children[1].style.border = "5px solid red";

// 4.4
document.body.style.fontSize = "50px";
