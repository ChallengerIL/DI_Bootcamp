// Exercise 3 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function (childrenNum, name, location, jobTitle) {
    const body = document.querySelector('body');
    const text = `You will be a ${jobTitle} in ${location}, and married to ${name} with ${childrenNum} kids.`;
    body.appendChild(document.createTextNode(text));
})(20, "Sarah", "Ashdod", "Janitor")
