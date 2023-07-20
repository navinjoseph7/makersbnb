from lib.user import User

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"], row["password"])
            users.append(item)
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', [
                                user.name, user.email, user.password])
        rows = self._connection.execute('SELECT * from users WHERE email = %s',[user.email])
        row = rows[0]
        if row['password']==user.password:
            print (row['id'])
            return row['id']
        else:
            return False
    def validate_user(self,email,password):
        rows = self._connection.execute('SELECT * from users WHERE email = %s',[email])
        row = rows[0]
        if row['password']==password:
            return row['id']
        else:
            return False
        
        