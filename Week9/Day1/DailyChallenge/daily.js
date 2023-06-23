// Instructions
// Create a form with two fields (name, last name) and a submit button.
// When you click the Send button, retrieve the data from the inputs, and append it on the DOM as a JSON string.
// The output should be:

const form = document.forms[0];
form.addEventListener("submit", buttonClick);

function buttonClick(event){
    event.preventDefault();

    let fd = new FormData(form);
    let data = {};

    for (let [key, prop] of fd) {
        data[key] = prop;
    }

    data = JSON.stringify(data);

    let body = document.querySelector('body');
    body.appendChild(document.createTextNode(data));
}
