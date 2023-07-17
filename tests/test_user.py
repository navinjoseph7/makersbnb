from lib.user import User

"""

"""
def test_user_constructs():
    user = User(1, "Testusername", "Testpassword", "Testfirstname", "Testsurname")
    assert user.id == 1
    assert user.user_name == "Testusername"
    assert user.password == "Testpassword"
    assert user.first_name == "Testfirstname"
    assert user.sur_name == "Testsurname"

"""
We can format Users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Testusername", "Testpassword", "Testfirstname", "TestSurname")
    assert str(user) == "User(1, Testusername, Testpassword, Testfirstname, TestSurname)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical Users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Testusername", "Testpassword", "Testfirstname", "TestSurname")
    user2 = User(1, "Testusername", "Testpassword", "Testfirstname", "TestSurname")
    assert user1 == user2