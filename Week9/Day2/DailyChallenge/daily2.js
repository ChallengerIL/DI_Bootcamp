// 2nd Daily Challenge
// const morse = `{
//   "0": "-----",
//   "1": ".----",
//   "2": "..---",
//   "3": "...--",
//   "4": "....-",
//   "5": ".....",
//   "6": "-....",
//   "7": "--...",
//   "8": "---..",
//   "9": "----.",
//   "a": ".-",
//   "b": "-...",
//   "c": "-.-.",
//   "d": "-..",
//   "e": ".",
//   "f": "..-.",
//   "g": "--.",
//   "h": "....",
//   "i": "..",
//   "j": ".---",
//   "k": "-.-",
//   "l": ".-..",
//   "m": "--",
//   "n": "-.",
//   "o": "---",
//   "p": ".--.",
//   "q": "--.-",
//   "r": ".-.",
//   "s": "...",
//   "t": "-",
//   "u": "..-",
//   "v": "...-",
//   "w": ".--",
//   "x": "-..-",
//   "y": "-.--",
//   "z": "--..",
//   ".": ".-.-.-",
//   ",": "--..--",
//   "?": "..--..",
//   "!": "-.-.--",
//   "-": "-....-",
//   "/": "-..-.",
//   "@": ".--.-.",
//   "(": "-.--.",
//   ")": "-.--.-"
// }`
// Create three functions. The two first functions should return a promise..

// The first function is named toJs():
// this function converts the morse json string provided above to a morse javascript object.
// if the morse javascript object is empty, throw an error (use reject)
// else return the morse javascript object (use resolve)

// The second function called toMorse(morseJS), takes one argument: the new morse javascript object.

// This function asks the user for a word or a sentence.
// if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
// else return an array with the morse translation of the user’s word.
// if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
// if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object


// The third function called joinWords(morseTranslation), takes one argument: the morse translation array

// this function joins the morse translation by using line break and display it on the page (ie. On the DOM)

// Chain the three functions.
// Example:
// "Hello" gives you
// ....
// .
// .-..
// .-..
// ---

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}`

const toJs = (morseJSON) => {
    return new Promise((resolve, reject) => {

        let obj = JSON.parse(morseJSON);

        if (Object.entries(obj).length != 0) {
            resolve(obj);
        } else {
            reject(new Error('The object is empty'));
        }
    });
};

const toMorse = (morseJS) => {
    return new Promise((resolve, reject) => {

        let input = prompt("Enter a word or a sentence", "");
        input = input.toLowerCase();

        let withoutSpaces = input.replace(/\s+/g, '');
        withoutSpaces = withoutSpaces.split("");

        if (withoutSpaces.every(element => Object.keys(morseJS).includes(element))) {
            let result = [];
            let withoutSpacesIndex = 0;
            for (let i=0; i < input.length; i++) {
                if (input[i] == " ") {
                    result.push(" ")
                    withoutSpacesIndex -= 1;
                } else {
                    result.push(morseJS[withoutSpaces[withoutSpacesIndex]]);
                }
                withoutSpacesIndex++;
            }
            
            resolve(result);
        } else {
            reject(new Error('Your input contains forbidden characters'));
        }
    });
};

function joinWords(morseTranslation) {
    const body = document.querySelector("body");
    for (let element of morseTranslation) {
        body.appendChild(document.createTextNode(element));
        let br = document.createElement("br");
        body.appendChild(br);
    }
}

toJs(morse).then(result => toMorse(result)).then(result => joinWords(result));
