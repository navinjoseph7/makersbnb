class Space:
    def __init__(self, id, name, description, price_per_night,availability_start_date,availability_end_date,owner_user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.availability_start_date = availability_start_date
        self.availability_end_date =availability_end_date
        self.owner_user_id = owner_user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.availability_start_date}, {self.availability_end_date}, {self.owner_user_id})"