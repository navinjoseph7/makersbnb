
class Booking:
    def __init__(self, space, user, date, status="Available"):
        self.space_id = space.id
        self.booked_user_id = user.id
        self.name = space.name
        self.date_booked = date
        self.status = status


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.space_id}, {self.booked_user_id}, {self.name}, {self.date_booked}, {self.status})"