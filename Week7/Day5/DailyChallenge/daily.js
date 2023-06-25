function getInput() {

    let inputNumber;
    do {
        inputNumber = parseInt(prompt("Enter a number", ""), 10);

        if (isNaN(inputNumber)) {
            alert("Not a number");
        } else {
            return inputNumber;
        }
    } while(isNaN(inputNumber) || inputNumber < 1);
}

function bottlesOfBeer() {

    let totalBottles = getInput();
    let decrement = 1;

    while (totalBottles > 0) {

        if (decrement > totalBottles) {
            decrement = totalBottles
        }
        
        console.log(`${totalBottles} bottles of beer on the wall`);
        console.log(`${totalBottles} bottles of beer`);
        console.log(`Take ${decrement} down, pass ${decrement > 1 ? 'them' : 'it'} around`);
        totalBottles -= decrement;
        console.log(`${totalBottles} bottles of beer on the wall`);
        decrement++;
    }
    
}

bottlesOfBeer()
