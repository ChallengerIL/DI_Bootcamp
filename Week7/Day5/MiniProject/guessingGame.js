function getInput() {

    let inputNumber;
    do {
        inputNumber = parseInt(prompt("Pick a number between 1 and 10", ""), 10);

        if (isNaN(inputNumber)) {
            alert("Sorry Not a number, Goodbye");
        } else if (inputNumber < 1 || inputNumber > 10) {
            alert("Sorry it's not a good number, Goodbye");
        } else {
            return inputNumber;
        }
    } while(isNaN(inputNumber) || inputNumber > 10 || inputNumber < 1);
}

function compareNumbers(userNumber,computerNumber) {

    if (userNumber == computerNumber) {
        alert("WINNER!");
        return true;
    } else if (userNumber > computerNumber) {
        alert("Your number is bigger then the computer's, guess again");
        return false;
    } else if (userNumber < computerNumber) {
        alert("Your number is smaller then the computer's, guess again");
        return false;
    }

}

function playTheGame() {

    let userNumber;
    let computerNumber;
    let tries = 3;

    if (confirm("Would you like to play the game?") == true) {

        computerNumber = Math.round(Math.random() * 10);

            while (tries > 0) {

                userNumber = getInput();
                if (userNumber) {

                    if (compareNumbers(userNumber, computerNumber)) {
                        return;
                    } else {
                        tries -= 1;
                        continue;
                    }
            }
        }

        alert("Out of chances");
        return;

    } else {
        alert("No problem, goodbye!");
    }

}
