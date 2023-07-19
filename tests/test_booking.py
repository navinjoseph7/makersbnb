from lib.booking import *
from lib.space import *
from lib.user import *

"""
When I create a booking, it constructs with the correct fields
"""

def test_create_booking():
    space = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    user = User(1, "Testname", "Testemail", "Testpassword")
    booking = Booking(space, user, '02/06/23', None)
    assert booking.space_id == 1
    assert booking.booked_user_id == 1
    assert booking.name == "Cornwall Beach Hut"
    assert booking.date_booked == "02/06/23"
    assert booking.status == None

"""
When we create a booking with the same details they are equal
"""

def test_equality():
    space = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    user = User(1, "Testname", "Testemail", "Testpassword")
    booking_1 = Booking(space, user, '02/06/23', None)
    booking_2 = Booking(space, user, '02/06/23', None)
    assert booking_1 == booking_2


"""
When I create a booking, I can get all the details back in a nice format
"""

def test_formatting():
    space = Space(1, "Cornwall Beach Hut", "Sunny beach hut for two near the coast", "85.00", '01/06/23', '01/07/23')
    user = User(1, "Testname", "Testemail", "Testpassword")
    booking = Booking(space, user, '02/06/23', None)
    assert str(booking) == 'Booking(1, 1, Cornwall Beach Hut, 02/06/23, None)'

   
