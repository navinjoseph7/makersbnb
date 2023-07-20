from lib.space import *
from lib.space_repository import *
from datetime import date

"""
When I call list_all() I get a list of all spaces 
"""

def test_list_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    print (repo.list_all())
    spaces= repo.list_all()
    space = spaces[0]
    print (type(space.availability_start_date))
    assert repo.list_all() == [
        Space(
            1, 
            "Cornwall Beach Hut", 
            "Sunny hut on coast", 
            85, 
            date.fromisoformat('2023-06-01'), 
            date.fromisoformat('2023-07-01'),
            1
        ),
        Space(
            2,
            'Norfolk Beach Hut',
            'Sunny hut in North East',
            85,
            date.fromisoformat('2023-06-01'), 
            date.fromisoformat('2023-07-01'),
            1
        ),    
        Space(
            3,
            'Suffolk Beach Hut',
            'Sunny hut in South', 
            85, 
            date.fromisoformat('2023-06-01'), 
            date.fromisoformat('2023-07-01'),
            1
        )
            ]
    
def test_space_create(db_connection):
        db_connection.seed("seeds/makersbnb.sql")
        repo = SpaceRepository(db_connection)
        result = repo.create(Space(None,"Whitechapel","London",60,date.fromisoformat('2023-06-01'),date.fromisoformat('2023-07-01'),2))
        assert result == True