// Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

function hotelCost() {

    let cost = 140;

    do {
        var nightsNum = parseInt(prompt("How many nights do you expect to stay with us?", ""), 10);
    } while(isNaN(nightsNum) || nightsNum < 1);

    return nightsNum * cost;

}

function planeRideCost() {

    do {
        var destination = prompt("What is your destination?", "");
    } while(destination.length == 0 || !isNaN(destination));

    let cost = 300;

    switch (destination){

        case 'London':
            cost = 183;
            break;
        case 'Paris':
            cost = 220;
            break;

      }

      return cost;

}

function rentalCarCost() {

    let cost = 40;
    let total = 0;
    let discountPercent = 5;

    do {
        var daysNum = parseInt(prompt("For how many days would you like to rent a car?", ""), 10);
    } while(isNaN(daysNum) || daysNum < 1);

    total = cost * daysNum;

    if (daysNum > 10) {
        let discount = total * (discountPercent/100);
        total -= discount
    }

    return total;

}

function totalVacationCost() {
    return hotelCost() + planeRideCost() + rentalCarCost()
}

totalVacationCost()
