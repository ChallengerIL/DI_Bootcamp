// Exercise 2 : Promises
// Instructions
// Create a promise that resolves itself in 4 seconds and returns a “success” string.
// How can you make your promise from part 1 shorter using Promise.resolve() and console.log “success”?
// Add code to catch errors and console.log ‘Ooops something went wrong’.

// 1
const promise1 = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Success");
        }, 4000);
    });
};

promise1().then(result => console.log(result)).catch(error => console.log(error));

// 2
setTimeout(() => {Promise.resolve("Success").then(result => console.log(result));}, 4000);
