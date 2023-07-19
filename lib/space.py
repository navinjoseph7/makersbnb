class Space:
    def __init__(self, id, name, description, price_per_night, availibility_start_date, availibility_end_date):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.availibility_start_date = availibility_start_date
        self.availibility_end_date = availibility_end_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.availibility_start_date}, {self.availibility_end_date})"