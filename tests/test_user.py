from lib.user import User

"""

"""
def test_user_constructs():
    user = User(1, "Testname", "Testemail", "Testpassword")
    assert user.id == 1
    assert user.name == "Testname"
    assert user.email == "Testemail"
    assert user.password == "Testpassword"


"""
We can format Users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Testname", "Testemail", "Testpassword")
    assert str(user) == "User(1, Testname, Testemail, Testpassword)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical Users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Testname", "Testemail", "Testpassword")
    user2 = User(1, "Testname", "Testemail", "Testpassword")
    assert user1 == user2