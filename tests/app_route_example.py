
'''
@app.route('/spaces/1')
    def book_a_space():
        create connection
        create bookings repo
        
        # Extract the space ID
        space_id = request.form['id']

        #Extract space name 
        space_name = request.form['name']

        # Extract the date user entered
        date = request.form['date']

        booking = Booking(space_id, space_name, date, "requested")
        repo.create(booking)
        
        redirect to bookings and requests page 
    
    

'''