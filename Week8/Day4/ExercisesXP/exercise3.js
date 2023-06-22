// Exercise 3: User & Id
// Instructions
// Using this object const users = { user1: 18273, user2: 92833, user3: 90315 }

// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.

// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]

const users = { user1: 18273, user2: 92833, user3: 90315 };

// 1
const usersArray = Object.entries(users);
// console.log(usersArray);

// 2
const newUsers = Object.fromEntries(usersArray);
for (let [key, value] of Object.entries(newUsers)) {
    newUsers[key] *= 2;
  }
const result = Object.entries(newUsers);
console.log(result);
