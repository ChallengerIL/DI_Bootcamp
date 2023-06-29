// Instructions
// Setup
// Create a new directory, and use npm init

// Create a new file named server.js,
// install and import express,
// install and import body-parser,
// install and import cors,
// install axios,
// install ejs,
// install and import rss-parser - a node.js module. See the documentation here

// We will use this RSS Fact Feed https://thefactfile.org/feed/

// Add the code below from the rss-parser documentation.
// replace the ‘your-rss-feed’ to the url given above. Make some tests to understand how it works and run the application.
// let Parser = require('rss-parser');
// let parser = new Parser();

// (async () => {

//   let feed = await parser.parseURL('your-rss-feed');
//   console.log(feed.title);

//   feed.items.forEach(item => {
//     console.log(item.title + ':' + item.link)
//   });

// })();

// Static Files
// Create a public directory, with tow subfolder : partials and pages.

// In the partials folder, create four ejs files:

// footer.ejs : contains a simple footer with the paragram “Copyright 2021 …”
// head.ejs : contains the CDN of Bootstrap, and some style in a <style> tag
// header.ejs : contains a Boostrap navbar with the links

//     <a class="nav-link" href="/">Home</a>
//     <a class="nav-link" href="/search">Search</a>
// posts.ejs : contains a div, where the posts are displayed. Each posts is composed of:

// a link that redirects the user to the specific post in the website https://www.thefactsite.com/
// the publication date, creator, category and content of the post

// In the pages folder, create two ejs files:

// search.ejs :
// It should include the files head.ejs, header.ejs, posts.ejs and footer.ejs.
// It should contain two forms, to search a post by title and by category (with options).
// index.ejs is the home page displaying all the posts.
// It should include the files head.ejs, header.ejs, posts.ejs and footer.ejs.

// The Server
// Create a few routes in the file server.js:
// / route : will retrieve all the facts from the RSS feed and render the posts in the index.ejs file. It’s a GET request.
// /search route: renders the search.ejs file. At first, no posts should be displayed. It’s a GET request.
// /search/title route: will retrieve the input (ie. chosen title) of the user, and render the correct post in the search.ejs file. It’s a POST request.
// /search/category route: will retrieve the input (ie. chosen category) of the user, and render the correct post in thesearch.ejs file. It’s a POST request.

const express = require('express');
const cors = require("cors");
const bp = require('body-parser');
let Parser = require('rss-parser');
var path = require('path');
const app = express();

app.set('views', path.join(__dirname, '/public/pages'));
app.set('view engine', 'ejs');

app.use(cors());
app.use(express.static(__dirname + '/public'));
app.use(bp.urlencoded({extended:false}));
app.use(bp.json());

let parser = new Parser();

app.get('/', (req, res) => {

    (async () => {

        let feed = await parser.parseURL('https://thefactfile.org/feed/');

        res.render('index', feed);
    })();
});

app.get('/search', (req, res) => {

    let categories = [];

    (async () => {

        let feed = await parser.parseURL('https://thefactfile.org/feed/');

        feed.items.forEach(item => {
            item.categories.forEach(category => {
                if (!categories.includes(category)) {
                    categories.push(category);
                };
            });
        });

        res.render('search', {items: [], categories: categories});
    })();
});

app.post('/search/', (req, res) => {

    let categories = [];
    let result = {items: [], categories: categories};

    (async () => {

        let feed = await parser.parseURL('https://thefactfile.org/feed/');
    
        feed.items.forEach(item => {
            item.categories.forEach(category => {
                if (!categories.includes(category)) {
                    categories.push(category);
                };
            });

            if ("searchTitle" in req.body) {
                if (item.title.includes(req.body.searchTitle) || item.content.includes(req.body.searchTitle)) {
                    result.items.push(item);
                }
            } else if ("searchCategory" in req.body) {
                if (item.categories.includes(req.body.searchCategory)) {
                    result.items.push(item);
                }
            }
        });
        res.render('search', result);
    })();
});

app.listen(3000);
