// Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.
// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?

// 1
// We'll get 3 in the alert because we reassigned the value of a after it passed our check

// 2
// funcThree will return an alert message with a 0 in it because the a variable is set to 0 at the moment
// funcTwo will reassign the value of a to 5 and that's it
// funcThree will return the new value, which is 5
// 2.2
// We will get an error because it's impossible to reassign a const

// 3
// funcFour creates in our window a new variable a with a value of 'Hello'
// funcFive displays an alert with that new variable

// 4
// The alert will contain the new value of "test" as we just reassigned it inside the function, right before calling the alert
// 4.2
// We will get an error because it's impossible to reassign a const

// 5
// We will get back two alerts. The first one will contain a value of 5 as we assigned it inside of the if-statement (using the let method). The second alert will contain the value of 2 because of the scope.
