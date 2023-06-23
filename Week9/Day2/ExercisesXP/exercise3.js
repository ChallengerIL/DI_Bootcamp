// Exercise 3 : Resolve & Reject
// Instructions
// Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
// Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”

// 1
Promise.resolve(3).then(result => console.log(result));

// 2
Promise.reject("Boo!").catch(error => console.log(error));
