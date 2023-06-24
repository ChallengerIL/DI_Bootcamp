// Instructions
// You should use this API: https://www.swapi.tech/ to get the data and update it “randomly” in your website by clicking a button.
// Note: The API contains 83 different characters

// Create your HTML file, and add the relevant elements.

// In your JS file, create your functions :
// to retrieve the elements from the DOM.
// to get the data from the API (star wars characters).
// to display the info on the DOM: the name, height, gender, birth year, and home world of the character.

// Display the data using AJAX. Make sure to display a loading message as follows:
// You can use any of these animation icons for the loading message.
// Fontawesome link :
// https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css

// 4. If there is an error getting the data, display a message as follows:

// 5. You can use your own css to style the website as you see fit

const infoContainer = document.querySelector(".info-container");
const button = document.querySelector("button");

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

function showLoading() {
    const div = document.createElement("div");
    div.className = "fa-3x";

    const i = document.createElement("i");
    i.className = "fa-solid fa-spinner fa-spin-pulse";

    const p = document.createElement("p");
    p.textContent = "Loading...";

    div.appendChild(i);

    infoContainer.appendChild(div);
    infoContainer.appendChild(p);

    // return new Promise(resolve => {
    //     setTimeout(function () {
    //         div.style.display = 'none';
    //         p.style.display = 'none';
    //         resolve();
    //     }, 1000);
    // });
}

const getCharacter = async () => {
    try {
        let endpoint = "https://www.swapi.tech/api/people/" + getRandomInt(1, 90); //+ getRandomInt(1, 84)
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Oh No! That person isn't available.")
        }

        return data.result;
    } catch (err) {
        return err;
    }
}

const getPlanet = async (id) => {
    try {
        let endpoint = "https://www.swapi.tech/api/planets/" + id;
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Something went wrong...")
        }

        return data.result.properties.name;
    } catch (err) {
        return err;
    }
}

button.addEventListener("click", function (event) {
    infoContainer.textContent = "";

    ( async () => {
        showLoading();
        // await showLoading();
        let character = await getCharacter();

        if (character instanceof Error) {
            const error = document.createElement("h1");
            error.textContent = character.message;
            infoContainer.textContent = "";
            infoContainer.appendChild(error);
        } else {
            character = character.properties;

            const planetId = /[^/]*$/.exec(character.homeworld)[0];

            let planet = await getPlanet(planetId);

            console.log(planet);

            const name = document.createElement("h1");
            name.textContent = character.name;

            const height = document.createElement("p");
            height.textContent = `Height: ${character.height}`;

            const gender = document.createElement("p");
            gender.textContent = `Gender: ${character.gender}`;

            const birthYear = document.createElement("p");
            birthYear.textContent = `Birth Year: ${character.birth_year}`;

            const homeWorld = document.createElement("p");
            homeWorld.textContent = `Home World: ${planet}`;

            infoContainer.textContent = "";
            infoContainer.appendChild(name);
            infoContainer.appendChild(height);
            infoContainer.appendChild(gender);
            infoContainer.appendChild(birthYear);
            infoContainer.appendChild(homeWorld);
        }
    } )();
 });
