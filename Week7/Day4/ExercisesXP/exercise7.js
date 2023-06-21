// Exercise 7 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.

const allBooks = [];
const book1 = {
    title: 'The Great Gatsby',
    author: 'F. Scott Fitzgerald',
    image: 'https://upload.wikimedia.org/wikipedia/commons/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg',
    alreadyRead: true
};
const book2 = {
    title: 'To Kill a Mockingbird',
    author: 'Harper Lee',
    image: 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRO7Te2MLyEC2TPkOt7Ghh_SpYdEyuYUsznDwdc-0qhy-Ju4v0I',
    alreadyRead: false
};
allBooks.push(book1, book2);

const section = document.querySelector('.booksList');

for(let book of allBooks) {
    let div = document.createElement('div');
    section.appendChild(div);

    let img = document.createElement('img');
    img.setAttribute("src", book.image);
    img.style.width = '100px';
    div.appendChild(img);

    let p = document.createElement('p');
    p.textContent = `${book.title} written by ${book.author}`;

    if (book.alreadyRead) {
        p.style.color = 'red';
    }

    div.appendChild(p);
}
