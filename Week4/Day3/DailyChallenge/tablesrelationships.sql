-- Tables Relationships
-- You are going to practice tables relationships

-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

-- Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive

-- Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- The number of customers that are not LoggedIn


-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee

-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);

-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14

-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

-- Display the data
-- Select all the columns from the junction table
-- Select the name of the student and the title of the borrowed books
-- Select the average age of the children, that borrowed the book Alice in Wonderland
-- Delete a student from the Student table, what happened in the junction table ?

-- 1.1
CREATE TABLE customer (
	id serial PRIMARY KEY,
	first_name VARCHAR ( 50 ) NOT NULL,
	last_name VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE customer_profile (
	id serial PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	customer_id INTEGER NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE RESTRICT
);

-- 1.2
INSERT INTO customer (first_name, last_name)
VALUES
	('John', 'Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive');

-- 1.3
INSERT INTO customer_profile (isloggedin, customer_id)
SELECT TRUE, customer.id
FROM customer
WHERE first_name = 'John';

INSERT INTO customer_profile (customer_id)
SELECT customer.id
FROM customer
WHERE first_name = 'Jerome';

-- 1.4
SELECT c.first_name, cp.isloggedin
FROM customer c
INNER JOIN customer_profile cp
USING (id)
WHERE cp.isloggedin;

SELECT c.first_name, cp.isloggedin
FROM customer c
FULL OUTER JOIN customer_profile cp
USING (id);

SELECT COUNT(*)
FROM customer c
FULL OUTER JOIN customer_profile cp
USING (id)
WHERE NOT cp.isloggedin;


-- 2.1
CREATE TABLE book (
	book_id serial PRIMARY KEY,
	title VARCHAR ( 100 ) NOT NULL,
	author VARCHAR ( 50 ) NOT NULL
);

-- 2.2
INSERT INTO book (title, author)
VALUES
	('Alice In Wonderland', 'Lewis Carroll'),
	('Harry Potter', 'J.K Rowling'),
	('To kill a mockingbird', 'Harper Lee');

-- 2.3
CREATE TABLE student (
	student_id serial PRIMARY KEY,
	name VARCHAR ( 100 ) NOT NULL UNIQUE,
	age SMALLINT CHECK (age <= 15)
);

-- 2.4
INSERT INTO student (name, age)
VALUES
	('John', 12),
	('Lera', 11),
	('Patrick', 10),
	('Bob', 14);

-- 2.5
CREATE TABLE library (
	book_fk_id INTEGER NOT NULL,
	student_fk_id INTEGER NOT NULL,
	FOREIGN KEY(book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY (book_fk_id, student_fk_id),
	borrowed_date DATE DEFAULT CURRENT_DATE
);

-- 2.6
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES 
	((SELECT book_id FROM book where title = 'Alice In Wonderland'), 
	(SELECT student_id FROM student where name = 'John'), '2022-02-15'),
	((SELECT book_id FROM book where title = 'To kill a mockingbird'), 
	(SELECT student_id FROM student where name = 'Bob'), '2021-03-03'),
	((SELECT book_id FROM book where title = 'Alice In Wonderland'), 
	(SELECT student_id FROM student where name = 'Lera'), '2021-05-23'),
	((SELECT book_id FROM book where title = 'Harry Potter'), 
	(SELECT student_id FROM student where name = 'Bob'), '2021-08-12');

-- 2.7
SELECT * FROM library;

SELECT s.name, b.title
FROM student s
INNER JOIN library l
ON s.student_id = l.student_fk_id
INNER JOIN book b
ON b.book_id = l.book_fk_id;

SELECT AVG(s.age)
FROM student s
INNER JOIN library l
ON s.student_id = l.student_fk_id
INNER JOIN book b
ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

DELETE FROM student
WHERE name = 'John';
-- The student's record got deleted
