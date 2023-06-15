// Exercise 4 : Building Management
// Instructions:
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }


// Review About Objects
// Copy and paste the above object to your Javascript file.

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

// 1
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

// 2
console.log(building['numberOfFloors'])

// 3
console.log(building['numberOfAptByFloor']['firstFloor'], building['numberOfAptByFloor']['thirdFloor'])

// 4
dan = building['nameOfTenants'][1].toLowerCase()
console.log(dan, building['numberOfRoomsAndRent'][dan][0])

// 5
sarah = building['nameOfTenants'][0].toLowerCase()
david = building['nameOfTenants'][2].toLowerCase()

sarahsRent = building['numberOfRoomsAndRent'][sarah][1]
davidsRent = building['numberOfRoomsAndRent'][david][1]
dansRent = building['numberOfRoomsAndRent'][dan][1]

if (sarahsRent + davidsRent > dansRent) {
    building['numberOfRoomsAndRent'][dan][1] = 1200;
  }

console.log(dansRent)
console.log(building['numberOfRoomsAndRent'][dan][1])
