// Exercise 6 : Challenges
// Evaluate these (ie True or False)

// [2] === [2] 
// {} === {}

// What is, for each object below, the value of the property number and why?

// const object1 = { number: 5 }; 
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number)
// console.log(object3.number)
// console.log(object4.number)

// Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin ect …

// Create a class Mamal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.

// Create a farmerCow object that is an instance of the class Mamal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
// For example: Moooo I'm a cow, named Lily and I'm brown and white

// 1
// console.log([2] === [2]); 
// console.log({} === {});

// 2
const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
console.log(object3.number)
console.log(object4.number)

// object1 started with a 5, which was later reassigned to a 4.
// The same story with object2, as it is a full copy of object1. The value gets reassigned as well.
// The same applies to object3.
// object4 retains it's initial value of 5.

class Animal {
    constructor(name, type, color) {
      this.name = name;
      this.type = type;
      this.color = color;
    }
}

class Mammal extends Animal {
    constructor(name,type, color) {
        super(name, type, color);
    }

    sound(animalsSound) {
        return `${animalsSound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
}

let farmerCow = new Mammal('Lily', 'cow', 'brown and white');
console.log(farmerCow.sound('moo'));
