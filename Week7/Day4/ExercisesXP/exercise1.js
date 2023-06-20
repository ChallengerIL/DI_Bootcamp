// Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313


// Bonus: Add a parameter divisor to the function.

// displayNumbersDivisible(divisor)

// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
// and their sum

function displayNumbersDivisible(divisor) {
    let arr = [];
    let divisible = [];
        for (i = 0; i <= 500; i++){
           arr.push(i);

           if (i % divisor === 0) {
            console.log(i)
            divisible.push(i)
           }

        };
        console.log('Sum: %d', divisible.reduce((pv, cv) => pv + cv, 0))
        return arr;
}

displayNumbersDivisible(23)
