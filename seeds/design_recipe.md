# Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORIES:


as airbnb I can allow people to login or signup as a user
I should be able to keep track of their names,username,password
as airbanb I can allow users to list spaces
I should be able to track the space_names,decription,price per night and dates available



```
Nouns:

User,name,username,password
spaces,space_name,description,pricepernight,dates_available
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| User                      name,username,password
| Space                     space_name,description,price_per_night,dates_available,booked

1. Name of the first table (always plural): `users` 

    Column names: `name,username,password

2. Name of the second table (always plural): `spaces` 

    Column names: space_name,description,price_per_night,dates_available,dates_booked

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
name:text
username:text
password:text


Table: spaces
id: SERIAL
space_name:text
description:text
price_per_night:integer
dates_booked:text
```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

```
# EXAMPLE

1. Can one space have many users? NO
2. Can one user have many spaces? YES
```

_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._
`.
foreign key on spaces with user_id as owner_user_id
```
# EXAMPLE

 


## 4. Write the SQL.

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text
  username text
  password text
);

-- Create the second table.
CREATE TABLE tags (
  id: SERIAL
  space_name text
  description text
  price_per_night integer
  dates_booked text
  constraint fk_tag foreign key(owner_user_id) references users(id) on delete cascade,
);

-- Create the join table.


```

## 5. Create the tables.

```bash
psql -h 127.0.0.1 database_name < posts_tags.sql
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_tables_many_to_many_design_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_tables_many_to_many_design_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_tables_many_to_many_design_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_tables_many_to_many_design_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Ftwo_tables_many_to_many_design_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->