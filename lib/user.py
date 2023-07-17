class User:

    def __init__(self, id,user_name, password,first_name,sur_name):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.sur_name = sur_name

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Album
    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.password}, {self.first_name}, {self.sur_name})"