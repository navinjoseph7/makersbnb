-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces;


-- Then, we recreate them

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL,
    password text
);

-- Create the second table.
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    space_name text,
    description text,
    price_per_night integer,
    dates_booked text,
    owner_user_id integer,
    constraint fk_user FOREIGN KEY(owner_user_id) references users(id) on delete cascade
);

INSERT INTO users(name,email,password) VALUES ('Test Name', 'testemail@mmm', 'pass')