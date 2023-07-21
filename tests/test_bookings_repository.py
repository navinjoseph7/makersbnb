from lib.space_repository import *
from lib.booking import *
from lib.bookings_repository import *
from datetime import date

"""
When we trying to create a booking, then we adding booking to the table
"""

def test_creating_booking(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    booking = Booking(1, 1, 'Sunny hut on coast', '01/06/23', 'Available')
    repository.create(booking)
    assert booking.id == 4

"""
When we call @all_confirmed we can see the all confirmed bookings 
"""


def test_all_confirmed_bookings(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    assert repository.list_all_booked() == [
        Booking(2, 1, 'Sunny hut in North East', date(2023, 2, 6), 'Confirmed')
    ]

"""
When we call @all_requested we can see the all requested bookings 
"""
def test_all_requested_bookings(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    assert repository.list_all_requested() == [
        Booking(3, 1, 'Sunny hut in South', date(2023, 3, 6), 'Requested')
    ]


"""
When we call BookingRepository#find
We get a single Booking object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingsRepository(db_connection)

    booking = repository.find(1)
    assert booking == Booking(1, 1, 'Sunny hut on coast', None, 'Available')

"""
When we request to book something, we check if the status changed
"""
def test_all_requested_bookings(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    repository.request_bookings(1, '01/06/23')
    booking = repository.find(1)
    assert booking == Booking(1, 1, 'Sunny hut on coast', date(2023, 1, 6), 'Requested')

"""
When we want to book the same day in the same arbnb, that already booked, we recieve a mistake
"""

def test_unavailable_date(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    result = repository.request_bookings(2,'02/06/23')
    assert result == "Sorry that date is not available"


"""
When we confirmed requested booking, we check if the status changed
"""
def test_confirm_booking(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingsRepository(db_connection)
    repository.confirm_booking(3, '03/06/23')
    booking = repository.find(3)
    assert booking == Booking(3, 1, 'Sunny hut in South', date(2023, 3, 6), 'Confirmed')
