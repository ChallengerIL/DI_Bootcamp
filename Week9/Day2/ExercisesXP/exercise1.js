// Exercise 1 : Comparison
// Instructions
// Create a function called compareToTen(num) that takes a number as an argument.
// The function should return a Promise:
// the promise resolves if the argument is less than or equal to 10
// the promise rejects if argument is greater than 10.
// Test:

// //In the example, the promise should reject
// compareToTen(15)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))

// //In the example, the promise should resolve
// compareToTen(8)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))

// let compareToTen = new Promise(function (resolve, reject) {
    // if (goodGrades > 90) {
    //     resolve("Computer");
    // } else if (goodGrades > 80 && goodGrades <= 89) {
    //     resolve("Phone");
    // } else {
    //     reject("I won't get the gift");
    // }
// });

const compareToTen = (num) => {
    return new Promise((resolve, reject) => {
  
        if (num <= 10) {
            resolve("Success");
        } else {
            reject("Failure");
        }
    });
};

//In the example, the promise should reject
compareToTen(15).then(result => console.log(result)).catch(error => console.log(error));

//In the example, the promise should resolve
compareToTen(8).then(result => console.log(result)).catch(error => console.log(error));
