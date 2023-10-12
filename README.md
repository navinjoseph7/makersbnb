# Makersbnb

A property booking website built using Ruby and Active Record. Users can list their own properties for rental as well as book other users' properties.

## Our Process

We started our process by creating our user stories.

## User Stories

### MVP

```
As a user
I want to be able to
List a new property

As a user
I want to be able to
Book a stay at a property

As a user
I want to be able to
List multiple spaces

As a user
I want to be able to
Offer a range of dates for my property
```

### Stretch Stories

```
As a user
I want to be able to
Name my space, provide a description and price

As a user
I should not be able to
Book a date that another user has already booked

As a user
I want to be able to
Approve or reject booking requests
```

The next stage was to decide on our database layout, the data we would to store and how we would group this together in tables.
![](./images/database-plan.png)
After this we set out the pages we would need to create to meet our MVP.
![](./images/mvp-wireframe.png)

Now we had scoped out the high level design as well as features required we broke each MVP feature down into small individual tickets to implement over the course of our first sprint.

We reserved our second sprint to implement our stretch goals.

## Features

- Users can sign up and log in.
- Users can list spaces for rent, including a name, description, price per night, and availability dates.
- Users can view all spaces available for a given date range.
- Users can request to book a space for a given date range.
- Users can approve or reject booking requests.
- Users can only book spaces if they are signed in.
