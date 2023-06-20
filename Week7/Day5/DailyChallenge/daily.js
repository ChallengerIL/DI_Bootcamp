function getInput(maxNum) {

    let inputNumber;
    do {
        inputNumber = parseInt(prompt("Enter a number", ""), 10);

        if (isNaN(inputNumber)) {
            alert("Not a number");
        } else if (inputNumber < 1 || inputNumber > maxNum) {
            alert("The number is out of range");
        } else {
            return inputNumber;
        }
    } while(isNaN(inputNumber) || inputNumber > maxNum || inputNumber < 1);
}

function bottlesOfBeer() {

    let totalBottles = 99;
    let increment = 0;
    let decrement;
    let noun = 'it';

    while (totalBottles > 0) {
        decrement = getInput(totalBottles) + increment;

        if (noun === 'it') {
            if (decrement > 1) {
                noun = 'them';
            }
        }

        if (decrement > totalBottles) {
            decrement = totalBottles
        }
        
        console.log(`${totalBottles} bottles of beer on the wall`);
        console.log(`${totalBottles} bottles of beer`);
        console.log(`Take ${decrement} down, pass ${noun} around`);
        totalBottles = totalBottles - decrement;
        console.log(`${totalBottles} bottles of beer on the wall`);
        increment += 1;
    }
    
}

bottlesOfBeer()
