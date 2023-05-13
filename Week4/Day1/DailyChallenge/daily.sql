-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?


-- 1
SELECT COUNT(*) FROM actors;

-- 2
-- We get 'ERROR:  invalid input syntax for type date: ""'
-- But empty strings for names pass just fine
