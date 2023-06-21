// Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>


// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>

const form = document.forms[0];
console.log(form);

// const fname = document.querySelector('#fname');
// const lname = document.querySelector('#lname');
console.log(fname);
console.log(lname);

// const form = document.forms[0];
const fname = form.elements.fname;
const lname = form.elements.lname;
console.log(fname);
console.log(lname);

// let form = document.forms[0];
form.addEventListener("submit", buttonClick);
function buttonClick(event){
    event.preventDefault();
}
// // use event.preventDefault(), why ?
// // To prevent the form from being submitted

function buttonClick(event){
    event.preventDefault();
    let fname = form.elements.fname.value;
    let lname = form.elements.lname.value;

    if (fname.length != 0 && lname.length != 0) {
        let answersList = document.querySelector('.usersAnswer');
        let liOne = document.createElement('li');
        let liTwo = document.createElement('li');
        liOne.appendChild(document.createTextNode(fname));
        liTwo.appendChild(document.createTextNode(lname));
        answersList.appendChild(liOne);
        answersList.appendChild(liTwo);
    }
}
