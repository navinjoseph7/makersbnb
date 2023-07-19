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
            row["name"], 
            row["description"], 
            row["price_per_night"],
            row["availibility_start_date"],
            row["availibility_end_date"])
            for row in rows
        ]
        

    def request_to_book():
        #parameter: Space
        #returns: Nothing 
        #side effects: adds request to users booking requests
        pass

    def create():
        #parameters: Space
        #returns: none
        #side-effects: adds space to database
        pass 