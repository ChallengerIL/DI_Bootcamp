// Instructions
// Use this Giphy API Random documentation. Use this API Key : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
// In the HTML file, add a form, containing an input and a button. This input is used to fetch gif depending on a specific category.
// In the JS file, create a program to fetch one random gif depending on the search of the user (ie. If the search is “sun”, append on the page one gif with a category of “sun”).
// The gif should be appended with a DELETE button next to it. Hint : to find the URL of the gif, look for the sub-object named “images” inside the data you receive from the API.
// Allow the user to delete a specific gif by clicking the DELETE button.
// Allow the user to remove all of the GIFs by clicking a DELETE ALL button.

let url = 'https://api.giphy.com/v1/gifs/random?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';

const func = async (endpoint) => {
    let data;
    try {
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Something went wrong...")
        }
    } catch (err) {
        console.log(err);
    }

    return data.data;
}

const form = document.forms[0];
form.addEventListener("submit", buttonClick);

const deleteAllButton = document.querySelector('#deleteAll')
deleteAllButton.addEventListener("click", function (event) {
    let div = document.getElementById('container');
    div.innerHTML = "";
 });

function buttonClick(event){
    event.preventDefault();
    
    let category = form.category.value;
    url += `&tag=${category}`;

    let mainDiv = document.querySelector('#container');

    async function addGif() {
        let gif = await func(url);

        let id = /[^/]*$/.exec(gif.embed_url)[0];
        let finalUrl = `https://i.giphy.com/media/${id}/giphy.webp`

        let div = document.createElement('div');
        let img = document.createElement('img');
        let button = document.createElement('button');
        
        div.id = id;
        img.src = finalUrl;
        div.appendChild(img);

        button.value = id;
        button.textContent = "Delete";
        div.appendChild(button);

        button.addEventListener("click", function (event) {
            let buttonClicked = event.target;
            let divToRemove = document.getElementById(buttonClicked.value);
            divToRemove.remove();
         });

        mainDiv.appendChild(div);
    }
    
    addGif();
}
