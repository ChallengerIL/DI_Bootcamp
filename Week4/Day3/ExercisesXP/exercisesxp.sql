-- Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- Get all films, even if they don’t have languages.
-- Get all languages, even if there are no films in those languages.

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?


-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.


-- 1.1
SELECT * FROM language;

-- 1.2
SELECT film.title, film.description, language.name
FROM film
FULL OUTER JOIN language
ON film.language_id = language.language_id;

-- 1.3
CREATE TABLE new_film(
	id serial PRIMARY KEY NOT NULL,
	name VARCHAR(100) NOT NULL
);

INSERT INTO
	new_film (name)
VALUES
	('The Shawshank Redemption'),
	('The Godfather'),
	('The Dark Knight'),
	('The Godfather Part II'),
	('12 Angry Men');

-- 1.4
CREATE TABLE customer_review(
	review_id serial NOT NULL,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(100) NOT NULL,
	score SMALLINT NOT NULL,
	review_text TEXT NOT NULL,
	last_update DATE NOT NULL DEFAULT CURRENT_DATE,
	PRIMARY KEY (review_id),
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE RESTRICT
);

-- 1.5

INSERT INTO
	customer_review (film_id, language_id, title, score, review_text)
VALUES
	(2, 1, 'A review for the movie titled The Godfather', 10, 'Some review text for The Godfather here'),
	(5, 1, 'A review for the movie titled 12 Angry Men', 9, 'Some review text for 12 Angry Men here');

-- 1.6
DELETE FROM new_film where id = 5;
-- The review got deleted because of the "ON DELETE CASCADE"


-- 2.1
UPDATE film
SET language_id = 4
WHERE film_id = 384;

-- 2.2
-- Foreign Keys: store_id, address_id
-- We have to provide the IDs required in order to correctly INSERT new elements

-- 2.3
DROP TABLE IF EXISTS customer_review;
-- Easy step, no other tables depended on this one

-- 2.4
SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

-- 2.5
SELECT *
FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
INNER JOIN rental
ON inventory.inventory_id = rental.inventory_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC;

-- 2.6.1
SELECT *
FROM film
INNER JOIN film_actor
USING(film_id)
INNER JOIN actor
USING (actor_id)
WHERE film.description ILIKE '%sumo wrestler%' AND CONCAT(actor.first_name, ' ', actor.last_name) = 'Penelope Monroe';

-- 2.6.2
SELECT *
FROM film
WHERE length < 60 AND rating = 'R' AND description ILIKE '%documentary%';

-- 2.6.3
SELECT DISTINCT ON (f.title) *
FROM film f
INNER JOIN inventory i
USING(film_id)
INNER JOIN rental r
USING (inventory_id)
INNER JOIN customer c
USING (customer_id)
INNER JOIN payment p
USING (customer_id)
WHERE CONCAT(c.first_name, ' ', c.last_name) = 'Matthew Mahan'
AND p.amount > 4
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 2.6.4
SELECT *
FROM film f
INNER JOIN inventory i
USING(film_id)
INNER JOIN rental r
USING (inventory_id)
INNER JOIN customer c
USING (customer_id)
INNER JOIN payment p
USING (customer_id)
WHERE CONCAT(c.first_name, ' ', c.last_name) = 'Matthew Mahan' AND f.title ILIKE '%boat%'
OR CONCAT(c.first_name, ' ', c.last_name) = 'Matthew Mahan' AND f.description ILIKE '%boat%'
ORDER BY f.replacement_cost DESC
LIMIT 1;
