-- Items & Orders
-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.

-- Bonus :
-- Create a table called users.
-- There should be a one to many relationship between the users table and the product_orders table.
-- Create a function that returns the total price for a given order of a given user.

-- 1
CREATE TABLE product_orders (
	order_id SERIAL PRIMARY KEY,
	created_on DATE NOT NULL
);

-- 2
CREATE TABLE items (
	item_id serial PRIMARY KEY,
    fk_order_id INTEGER NOT NULL,
	price INTEGER NOT NULL,
    FOREIGN KEY (fk_order_id) REFERENCES product_orders(order_id)
);

INSERT INTO product_orders (created_on)
VALUES 
	('2022-02-20'),
	('2023-07-12'),
	('2021-11-11');

INSERT INTO items (fk_order_id, price)
SELECT product_orders.order_id, 99
FROM product_orders
WHERE product_orders.order_id = 1;

INSERT INTO items (fk_order_id, price)
SELECT product_orders.order_id, 50
FROM product_orders
WHERE product_orders.order_id = 1;

INSERT INTO items (fk_order_id, price)
SELECT product_orders.order_id, 27
FROM product_orders
WHERE product_orders.order_id = 3;



-- 3
CREATE or REPLACE FUNCTION get_full_amount(product_orders_id INTEGER) RETURNS INTEGER AS $fullamount$
BEGIN
   RETURN(SELECT SUM(items.price)) FROM items INNER JOIN product_orders ON items.fk_order_id = product_orders.order_id WHERE items.fk_order_id = product_orders_id;
END;
$fullamount$ LANGUAGE plpgsql;
