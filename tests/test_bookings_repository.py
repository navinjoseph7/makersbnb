from lib.space_repository import *
from lib.booking import *
from lib.bookings_repository import *



"""
When we call @all_confirmed we can see the all confirmed bookings 
"""

# def test_all_confirmed_bookigns(db_connection):
#     db_connection.seed('seeds/makersbnb.sql')
#     repository = BookingsRepository(db_connection)
#     assert repository.list_all() == [
#         Booking( 1, 1, "Cornwall Beach Hut", '01/06/23', None),
#         Booking( 2, 1, "North Folk", '02/06/23', "Confirmed"),
#         Booking( 3, 1, "South Folk", '03/06/23', "Requested")
#     ]

