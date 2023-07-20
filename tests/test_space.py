from lib.space import *

"""
When I create a space, it constructs with all the correct fields 
"""

def test_create_space_with_all_fields():
    space = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    assert space.id == 1
    assert space.name == "Cornwall Beach Hut"
    assert space.description == "Sunny beach hut for two near the coast"
    assert space.price_per_night == "85.00"
    assert space.availability_start_date == '01/06/23'
    assert space.availability_end_date == '01/07/23'

"""
When I created two spaces with the same details, they are equal
"""

def test_equality():
    space1 = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    space2 = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    assert space1 == space2

"""
When I create a space, I can get all the details back in a nice format
"""

def test_formatting():
    space = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    assert str(space) == 'Space(1, Cornwall Beach Hut, Sunny beach hut for two near the coast, 85.00, 01/06/23, 01/07/23)'