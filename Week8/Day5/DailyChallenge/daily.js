// Instructions
// Create a function that:

// takes in two strings as two parameters
// and returns a boolean that indicates whether or not the first string is an anagram of the second string.
// Some Help

// What is an anagram?
// An anagram is another word or phrase formed by rearranging letters of the first word or phrase.


// Example of anagrams

// "Astronomer" is an anagram of "Moon starer"
// "School master" is an anagram of "The classroom"
// "The Morse Code" is an anagram of "Here come dots"


// Do we need to consider whitespace?
// Trim whitespace prior to comparison.

let sortString = (string) => {
    return string.split("").sort().join("");
  };
    

function isAnagram(first, second) {
    first = first.toLowerCase();
    second = second.toLowerCase();

    first = first.replace(/\s+/g, '');
    second = second.replace(/\s+/g, '');

    first = sortString(first);
    second = sortString(second);

    return first === second;
}

console.log(isAnagram("School master", "The classroom"));
