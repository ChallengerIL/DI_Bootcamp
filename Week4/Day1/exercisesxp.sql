-- 1
CREATE DATABASE public;

-- 2
CREATE TABLE items (
	item_id SERIAL PRIMARY KEY,
	item VARCHAR(50) NOT NULL,
	price SMALLINT NOT NULL
);

CREATE TABLE customers (
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL
);

-- 3
INSERT INTO 
    items (item, price)
VALUES
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);
	
INSERT INTO 
    customers (first_name, last_name)
VALUES
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson');

-- 4
SELECT * FROM items;

-- 5
SELECT * FROM items WHERE price > 80;

-- 6
SELECT * FROM items WHERE price <= 300;

-- 7
SELECT * FROM customers WHERE last_name = 'Smith';

-- 8
SELECT * FROM customers WHERE last_name = 'Jones';

-- 9
SELECT * FROM customers WHERE first_name != 'Scott';