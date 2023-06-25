// Instructions
// You will create a currencies converter:

// image




// In this application we’re going receive data from two asynchronous sources.

// You will use :

// This documentation
// Create your own API key by signing up - you will be able to make more requests :)


// Note
// The program should take the currency which the user currently has and the currency in which they would like to receive, as well as the amount of money. Afterwards, the program will output the correct exchange rate based on the data from the APIs.

// First, you need to fetch all the supported currencies, in order to add the currencies options (ie FROM - To) in the currency converter. Check out this page on Supported Codes Endpoint from the ExchangeRate API documentation.

// To convert from a currency, to another one, you need to fetch conversion rate from the Pair Conversion API endpoint. Check out this page on Pair conversion requests from the ExchangeRate API documentation.
// Hint: You could also supply an optional AMOUNT variable in the query of the request.

// Bonus: Add this “switch” button on the page, when clicked on it will switch the currencies and display the new amount converted.
// Example : if the conversion was from EUR to GBP, as soon as the button is clicked on, the conversion should be from GBP to EUR.

const api = "d61a5dd9340857051af1af77";
let selectFrom = document.querySelector("#from");
let selectTo = document.querySelector("#to");
let amount = document.querySelector("#amount");
let output = document.querySelector("output");

const getCurrencies = async () => {
    try {
        let endpoint = `https://v6.exchangerate-api.com/v6/${api}/codes`;
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Something went wrong...")
        }

        return data.supported_codes;
    } catch (err) {
        return err;
    }
}

const convert = async (convertFrom, convertTo, convertAmount) => {
    try {
        let endpoint =  `https://v6.exchangerate-api.com/v6/${api}/pair/${convertFrom}/${convertTo}/${convertAmount}`;
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Something went wrong...")
        }

        return data.conversion_result;
    } catch (err) {
        return err;
    }
}

const switchCurrencies = async () => {
    let first = document.querySelector("#from").value;
    let second = document.querySelector("#to").value;

    document.querySelector("#from").value = second;
    document.querySelector("#to").value = first;

    if (output.textContent != "") {
        output.textContent = await convert(first, second, amount.value);
    }
}

const button = document.querySelector("#convert");

button.addEventListener("click", function (event) {
    ( async () => {
        const amountToCheck = amount.value;

        const conversionResult = await convert(selectFrom.value, selectTo.value, amountToCheck);

        output.textContent = conversionResult;
    } )();
 });

( async () => {
    let currencies = await getCurrencies();
    
    for (let currency of currencies) {
        let optionFrom = document.createElement("option");
        optionFrom.value = currency[0];
        optionFrom.textContent = `${currency[0]} - ${currency[1]}`;
        selectFrom.appendChild(optionFrom);

        let optionTo = document.createElement("option");
        optionTo.value = currency[0];
        optionTo.textContent = `${currency[0]} - ${currency[1]}`;
        selectTo.appendChild(optionTo);
    }
} )();
