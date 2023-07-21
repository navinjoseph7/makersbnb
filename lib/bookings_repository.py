from lib.booking import *

class BookingsRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (space_id, booked_user_id, space_name, date_booked, status) VALUES (%s, %s, %s, %s, %s) RETURNING id',
            [booking.space_id, booking.booked_user_id, booking.name, booking.date_booked, booking.status])
        booking.id =rows[0]['id']
        return booking
    
    def list_all_booked(self):
        # status = 'Confirmed'
        rows = self._connection.execute('SELECT * FROM bookings WHERE status = %s', ['Confirmed'])
        print(rows)
        return [Booking(row['space_id'], row['booked_user_id'], row['space_name'], row['date_booked'], row['status']) for row in rows]
    
    
    def list_all_requested(self):
        # status = 'Requested'
        rows = self._connection.execute('SELECT * FROM bookings WHERE status = %s', ['Requested'])
        return [Booking(row['space_id'], row['booked_user_id'], row['space_name'], row['date_booked'], row['status']) for row in rows]
    
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row['space_id'], row['booked_user_id'], row['space_name'], row['date_booked'], row['status'])
    
    def request_bookings(self, booking_id, date_booked):
        date_requested = self._connection.execute('SELECT EXISTS(SELECT 1 FROM bookings WHERE id = %s and date_booked = %s and status = %s)', [booking_id, date_booked, 'Confirmed'])
        if date_requested[0]['exists'] == True:
            return "Sorry that date is not available"
        else:
            self._connection.execute('UPDATE bookings SET status = %s, date_booked = %s WHERE id = %s', ['Requested', date_booked, booking_id])

    def confirm_booking(self, booking_id, date_booked):
        date_requested = self._connection.execute('SELECT EXISTS(SELECT 1 FROM bookings WHERE id = %s and date_booked = %s and status = %s)', [booking_id, date_booked, 'Confirmed'])
        if date_requested[0]['exists'] == True:
            return "Sorry that date is not available"
        else:
            self._connection.execute('UPDATE bookings SET status = %s, date_booked = %s WHERE id = %s', ['Confirmed', date_booked, booking_id])

    

                
