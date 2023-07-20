from lib.booking import *
from lib.space import *
from lib.user import *

"""
When I create a booking, it constructs with the correct fields
"""

def test_create_booking():
    booking = Booking(1, 1, "Cornwall Beach Hut", '02/06/23')
    assert booking.space_id == 1
    assert booking.booked_user_id == 1
    assert booking.name == "Cornwall Beach Hut"
    assert booking.date_booked == "02/06/23"
    assert booking.status == "Available"

"""
When we create a booking with the same details they are equal
"""

def test_equality():
    booking1 = Booking(1, 1, "Cornwall Beach Hut", '02/06/23')
    booking2 = Booking(1, 1, "Cornwall Beach Hut", '02/06/23')
    assert booking1 == booking2


"""
When I create a booking, I can get all the details back in a nice format
"""

def test_formatting():
    booking = Booking(1, 1, "Cornwall Beach Hut", '02/06/23')
    assert str(booking) == 'Booking(1, 1, Cornwall Beach Hut, 02/06/23, Available)'

   
