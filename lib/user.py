class User:

    def __init__(self, id,name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Album
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.password})"