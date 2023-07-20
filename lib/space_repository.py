from lib.space import *

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection 

    def list_all(self):
        #parameters: none
        #returns: accesses list of spaces from database and returns all 
        rows = self._connection.execute('SELECT * FROM spaces')
        return [
            Space(
            row["id"], 
            row["space_name"], 
            row["description"], 
            row["price_per_night"],
            row["availability_start_date"],
            row["availability_end_date"],
            row["owner_user_id"])
            for row in rows
        ]
        

    def request_to_book():
        #parameter: Space
        #returns: Nothing 
        #side effects: adds request to users booking requests
        pass

    def create(self,space):
        self._connection.execute('INSERT INTO spaces(space_name,description,price_per_night,availability_start_date,availability_end_date,owner_user_id) VALUES (%s, %s, %s, %s, %s, %s)', [ 
            space.name,
            space.description,
            space.price_per_night,
            space.availability_start_date,
            space.availability_end_date,
            space.owner_user_id

        ])
        return True

        #parameters: Space
        #returns: none
        #side-effects: adds space to database
        