from lib.space import *
from lib.space_repository import *

"""
When I call list_all() I get a list of all spaces 
"""

def test_list_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    assert repo.list_all() == [
        Space(
                1, 
                "Cornwall Beach Hut", 
                "Sunny beach hut for two near the coast", 
                "85.00", 
                '01/06/23', 
                '01/07/23')
    ]