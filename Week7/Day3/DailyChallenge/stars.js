// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

// 1
let star = "";

for (var i = 1; i < 7; i++){
    star += "*"
    console.log(star)
   }

// 2
let new_star = "\n";

for(var i=1; i <= 6; i++) {
    for(var j=1; j<=i; j++) {
        new_star += '*'
    }
    new_star += "\n";
}

console.log(new_star);
