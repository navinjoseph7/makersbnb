from lib.userrepository import UserRepository
from lib.user import User

def test_all(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    users = repository.all() # Get all artists

    # Assert on the results
    assert users == [User(1, "Test Name", "testemail@mmm","pass")]

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Navin Joseph", "navinmanisseril7@gmail.com","nopassword"))
    result = repository.all()
    assert result == [
        User(1, "Test Name", "testemail@mmm","pass"),
        User(2, "Navin Joseph", "navinmanisseril7@gmail.com","nopassword")
    ]

def test_validate_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    result =repository.validate_user("testemail@mmm","pass")
    assert result == True

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""

