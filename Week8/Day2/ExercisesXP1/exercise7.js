// Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// Create a Bootstrap Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.

const profilePicture = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png";

(function (name) {
    const nav = document.querySelector("nav");
    const span = document.querySelector(".navbar-text");
    const div = document.createElement('div');
    const img = document.createElement('img');

    nav.appendChild(div);
    span.appendChild(document.createTextNode(name));

    img.setAttribute("src", profilePicture);
    img.style.width = '50px';
    span.appendChild(img);

})("John")
