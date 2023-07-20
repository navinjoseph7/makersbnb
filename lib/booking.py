
class Booking:
    def __init__(self, space_id, user_id, space_name, date, status="Available"):
        self.space_id = space_id
        self.booked_user_id = user_id
        self.name = space_name
        self.date_booked = date
        self.status = status


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.space_id}, {self.booked_user_id}, {self.name}, {self.date_booked}, {self.status})"
    

        
    # def __init__(self, space_id, user_id, date, status="Available"):
    #     self.space_id = space_id
    #     self.booked_user_id = user_id
    #     self.name = space_name
    #     self.date_booked = date
    #     self.status = status