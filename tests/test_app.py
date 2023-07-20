from playwright.sync_api import Page, expect
from datetime import date, datetime
# Tests for your routes go here

# Homepage GET /home


"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."

    expect(strong_tag).to_have_text("Welcome to MakersBnB.")
    
def test_login_validation(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name=username]',"testemail@mmm")
    page.fill('input[name=password]',"pass")
    page.click('text=Log In')
    heading = page.locator('h1')
    expect(heading).to_have_text('What would you like to do?')
    link_to_book = page.locator('.t-book')
    expect(link_to_book).to_have_text("Book a space")


"""
Once a user is logged in, they see the homepage where they can choose to list or book a space
"""
def test_load_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/homepage")
    heading = page.locator('h1')
    expect(heading).to_have_text('What would you like to do?')
    link_to_book = page.locator('.t-book')
    expect(link_to_book).to_have_text("Book a space")

# def test_get_sign_up(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/signup")
#     create_tag = page.locator("t-create_button")
#     expect(create_tag).to_have_value("Create User")

def test_post_signup(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/signup")
    page.fill('input[name=name]',"Hazel")
    page.fill('input[name=password]',"1234")
    page.fill('input[name=email]',"hazel@1234")
    page.click('text=Create User')
    heading = page.locator('h1')
    expect(heading).to_have_text('What would you like to do?')
    link_to_book = page.locator('.t-book')
    expect(link_to_book).to_have_text("Book a space")

def test_load_list_a_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/list")
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("List a New Space")

def test_post_list_a_space(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/list")
    page.fill('input[name=spaceName]',"WhiteChapel")
    page.fill('input[name=description]',"Place in London")
    page.fill('input[name=pricePerNight]','50')
    page.fill('input[name=startDate]','2023-08-01')
    page.fill('input[name=endDate]','2023-09-01')
    page.click('text=Confirm new Space')
    heading = page.locator('h1')
    expect(heading).to_have_text('What would you like to do?')
    link_to_book = page.locator('.t-book')
    expect(link_to_book).to_have_text("Book a space")


#def test_load_all_spaces(page, test_web_address, db_connection):
   # db_connection.seed('seeds/makersbnb.sql')
    #page.goto(f"http://{test_web_address}/spaces")
    
    


#def test_get_list(page, test_web_address, db_connection):
#  db_connection.seed('seeds/makersbnb.sql')
#    page.goto(f"http://{test_web_address}/list")

