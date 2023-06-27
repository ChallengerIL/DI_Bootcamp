// Exercise 5 : Bank Details
// Instructions
// In this exercise, you have to decide which type of variables you have to use (ie. let or const):

// Create a global variable called bankAmount which value is the amount of money currently in your account.
// Create a variable that saves the % amount of VAT (In Israel, it’s 17%).
// Create an array with all your monthly expenses, both positive and negative (money made and money spent).
// Example : const details = ["+200", "-100", "+146", "+167", "-2900"]
// Create a program that modifies the expenses (ie. the positive AND the negative expenses) so that they will include taxes (multiply each expense by the VAT).
// Display your current bankAccount standing at the end of the month.

let bankAmount = 10000;
const vat = 17;
const details = ["+200", "-100", "+146", "+167", "-2900"];

for (let amount of details) {
    let operator = amount.charAt(0);
    let total = amount.slice(1);
    let finalTotal = total * ((100 + vat) / 100);
    bankAmount = eval(`${bankAmount} ${operator} ${finalTotal}`); 
}

console.log(bankAmount);
